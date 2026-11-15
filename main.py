
# Dead Signal
# MS539 - Core Developer Track

# This file is where the game starts.
# It brings together the functions from the other Python files
# so the game can run without putting everything in one file.

# These imports let me use functions that I created in player.py.
from player import create_player, mission_result, show_status, change_resource

# This import lets me use the hallway function from world.py.
from world import hallway


def introduction() -> str:
    """
    This function introduces the player to the game.
    It also asks for their name and sends that name back.
    """

    # Print the game title and explain what is happening.
    print("========== DEAD SIGNAL ==========")
    print("Year: 2042 | Underground Research Facility")
    print("A network failure has triggered an emergency lockdown.")
    print("Restore the security network and escape before time runs out.")

    # Ask the player for their name.
    # The strip() removes extra spaces at the beginning or end.
    # return sends the name back to where the function was called.
    return input("Enter your name: ").strip()


def main() -> None:
    """
    This is the main function that runs the game.
    It creates the player, starts the game loop,
    and displays the ending when the game is finished.
    """

    # Call introduction() to get the player's name.
    # Then create_player() uses that name to set up the player.
    player = create_player(introduction())

    # Welcome the player using the name they entered.
    print(f"\nWelcome, {player['name']}. Your mission begins now.")

    # Show the player's starting health, time, security, and inventory.
    show_status(player)

    # This is the first event in the game.
    # Five minutes pass and the security alert goes up.
    print("\nFive minutes pass as the security alert increases.")

    # These functions update the values stored in the player dictionary.
    # -5 removes five minutes.
    # 5 adds five points to the security alert.
    change_resource(player, "time", -5)
    change_resource(player, "security", 5)

    # This variable controls whether the game keeps running.
    playing = True

    # The while loop keeps running as long as the player is playing
    # and the mission has not ended.
    while playing and mission_result(player) == "ONGOING":

        # The hallway function displays the menu and handles a choice.
        # It returns True to keep playing or False to stop.
        playing = hallway(player)

    # Once the loop stops, the game displays the mission results.
    print("\n========== MISSION STATUS ==========")

    # Get the result of the player's mission.
    result = mission_result(player)

    # If the mission is still ongoing, the player chose to quit.
    # Otherwise, display the win or lose message.
    print("Mission ended voluntarily." if result == "ONGOING" else result)

    # Show the player's final resources and inventory.
    show_status(player)

    # Thank the player for playing the game.
    print(f"Thank you for playing, {player['name']}.")


# This checks whether main.py is being run directly.
# If it is, Python will start the game by calling main().
# It also prevents the game from starting automatically
# if main.py is imported into another Python file.
if __name__ == "__main__":
    main()
