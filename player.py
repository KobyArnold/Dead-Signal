
"""Player resources, inventory, and status displays for Dead Signal."""


def create_player(name: str) -> dict:
    """Create the player's starting resources and inventory."""
    return {
        "name": name or "Unknown Specialist",
        "health": 100,
        "security": 10,
        "time": 60,
        "integrity": 75.5,
        "inventory": [],
        "searched_lockers": [],
        "terminal_restored": False,
        "network_restored": False,
        "escaped": False,
    }


def change_resource(player: dict, resource: str, amount: float) -> float:
    """Change a resource, keeping it between zero and its maximum."""
    maximum = 100
    player[resource] = max(0, min(maximum, player[resource] + amount))
    return player[resource]


def collect_item(player: dict, item: str) -> bool:
    """Add an item once; return whether it was newly collected."""
    if item in player["inventory"]:
        return False

    player["inventory"].append(item)
    return True


def show_status(player: dict) -> None:
    """Display current resources and collected equipment."""
    print("\n========== PLAYER STATUS ==========")
    print(f"Specialist: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Security Alert: {player['security']}/100")
    print(f"Time Remaining: {player['time']} minutes")
    print(f"System Integrity: {player['integrity']:.1f}%")
    print("Inventory:", ", ".join(player["inventory"]) or "Empty")
    print("Terminal Restored:", player["terminal_restored"])
    print("Network Restored:", player["network_restored"])


def use_medkit(player: dict) -> bool:
    """Consume a medical kit and restore up to 25 health."""
    if "Medical Kit" not in player["inventory"] or player["health"] >= 100:
        return False

    player["inventory"].remove("Medical Kit")
    change_resource(player, "health", 25)
    return True


def mission_result(player: dict) -> str:
    """Return the current mission outcome or ongoing status."""
    if player["time"] <= 0:
        return "LOSE: Permanent lockdown activated."

    if player["health"] <= 0:
        return "LOSE: Your health reached zero."

    if player["security"] >= 100:
        return "LOSE: Automated security captured you."

    if player["escaped"]:
        return "WIN: You restored the network and escaped!"

    return "ONGOING"
