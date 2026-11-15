
"""Location menus, player choices, and random encounters."""

import random
from player import change_resource, collect_item, show_status, use_medkit


def get_choice(prompt: str, options: tuple[str, ...]) -> str:
    """Keep asking until the player enters an available menu choice."""
    while True:
        choice = input(prompt).strip()

        if choice in options:
            return choice

        print("Invalid choice. Choose:", ", ".join(options))


def random_event(player: dict) -> None:
    """Occasionally trigger an environmental hazard after a search."""
    event = random.choice(["clear", "clear", "sparks", "alarm"])

    if event == "sparks":
        print("Sparks erupt from damaged wiring! You lose 10 health.")
        change_resource(player, "health", -10)

    elif event == "alarm":
        print("A motion sensor activates! Security alert increases by 10.")
        change_resource(player, "security", 10)

    else:
        print("The area is quiet. No additional danger detected.")


def search_locker(player: dict, locker: str) -> None:
    """Collect a locker item once and apply the search time cost."""
    items = {
        "1": "Level 2 Keycard",
        "2": "Medical Kit",
        "3": "Repair Tools"
    }

    item = items[locker]

    if locker in player["searched_lockers"]:
        print("This locker has already been searched.")
        return

    change_resource(player, "time", -5)
    collect_item(player, item)
    player["searched_lockers"].append(locker)

    print(f"You found: {item}. Searching consumed 5 minutes.")

    if player["time"] > 0:
        random_event(player)


def storage_room(player: dict) -> None:
    """Let the player search lockers and return to the hallway."""
    while (
        player["time"] > 0
        and player["health"] > 0
        and player["security"] < 100
    ):
        print("\n========== STORAGE ROOM ==========")
        print("1. Locker A - Security Equipment")
        print("2. Locker B - Medical Supplies")
        print("3. Locker C - Maintenance Equipment")
        print("4. Return to Hallway")

        choice = get_choice("Choose (1-4): ", ("1", "2", "3", "4"))

        if choice == "4":
            return

        search_locker(player, choice)


def security_terminal(player: dict) -> None:
    """Require a keycard and allow one terminal restoration."""
    print("\n========== SECURITY TERMINAL ==========")

    if "Level 2 Keycard" not in player["inventory"]:
        print("ACCESS DENIED: Level 2 security keycard required.")

    elif player["terminal_restored"]:
        print("The terminal has already been restored.")

    else:
        change_resource(player, "time", -10)

        if player["time"] <= 0:
            print("The lockdown completes before you finish repairs!")
            return

        change_resource(player, "security", -5)
        player["terminal_restored"] = True

        print("ACCESS GRANTED. Security terminal restored!")


def server_room(player: dict) -> None:
    """Use repair tools to restore the network after terminal access."""
    print("\n========== SERVER ROOM ==========")

    if not player["terminal_restored"]:
        print("The server room remains locked until the terminal is restored.")

    elif "Repair Tools" not in player["inventory"]:
        print("You need repair tools from the storage room.")

    elif player["network_restored"]:
        print("The network is already restored.")

    else:
        change_resource(player, "time", -10)

        if player["time"] <= 0:
            print("The lockdown completes before the network can reboot!")
            return

        change_resource(player, "integrity", 24.5)
        player["network_restored"] = True

        print("Network restored! Emergency exit controls are online.")


def emergency_exit(player: dict) -> None:
    """Let the player escape only after restoring the network."""
    print("\n========== EMERGENCY EXIT ==========")

    if not player["network_restored"]:
        print("Exit locked. Restore the main network first.")

    else:
        player["escaped"] = True
        print("The emergency doors open. You reach the surface!")


def hallway(player: dict) -> bool:
    """Display the main menu and process one player action."""
    print("\n========== MAIN HALLWAY ==========")
    print("1. Access Security Terminal")
    print("2. Enter Storage Room")
    print("3. Enter Server Room")
    print("4. Approach Emergency Exit")
    print("5. View Player Status")
    print("6. Use Medical Kit")
    print("7. End Exploration")

    choice = get_choice("Choose (1-7): ", tuple("1234567"))

    if choice == "1":
        security_terminal(player)

    elif choice == "2":
        storage_room(player)

    elif choice == "3":
        server_room(player)

    elif choice == "4":
        emergency_exit(player)

    elif choice == "5":
        show_status(player)

    elif choice == "6":
        if use_medkit(player):
            print("Medical kit used. Health restored by up to 25.")
        else:
            print("No medical kit available, or health is already full.")

    else:
        print("You ended the investigation.")
        return False

    return True
