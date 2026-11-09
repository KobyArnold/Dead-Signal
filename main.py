
# ==========================================
# DEAD SIGNAL
# MS539 - Core Developer Track
# ==========================================

# Game Introduction
print("========== DEAD SIGNAL ==========")
print("Year: 2042")
print("Location: Underground Research Facility")
print()
print("A major network failure has triggered an emergency lockdown.")
print("Your objective is to restore the security network and escape.")
print()

# Player Information
player_name = input("Enter your name: ").strip()

if player_name == "":
    player_name = "Unknown Specialist"

print()
print(f"Welcome, {player_name}. Your mission begins now.")

# Player State Variables
health = 100
security_level = 10
time_remaining = 60
has_keycard = False
has_medkit = False
has_tools = False
system_integrity = 75.5
terminal_restored = False
exploring = True

# Display Starting Player Status
print()
print("========== PLAYER STATUS ==========")
print(f"Health: {health}")
print(f"Security Alert: {security_level}/100")
print(f"Time Remaining: {time_remaining} minutes")
print(f"Security Keycard: {has_keycard}")
print(f"Medical Kit: {has_medkit}")
print(f"Repair Tools: {has_tools}")
print(f"System Integrity: {system_integrity}%")

# Facility Lockdown Update
print()
print("========== FACILITY UPDATE ==========")
print("The facility's automated security system is still active.")
print("While you investigate, 5 minutes pass.")
print("The security alert level increases by 5.")

time_remaining = time_remaining - 5
security_level = security_level + 5

print()
print(f"Security Alert: {security_level}/100")
print(f"Time Remaining: {time_remaining} minutes")

# Main Game Loop
while exploring and time_remaining > 0 and security_level < 100:

    print()
    print("========== MAIN SECURITY HALLWAY ==========")
    print("You stand in the facility's main security hallway.")
    print("A damaged security terminal is beside a storage room.")
    print()
    print("1. Access Security Terminal")
    print("2. Enter Storage Room")
    print("3. View Player Status")
    print("4. End Exploration")
    print()

    choice = input("Enter your choice (1-4): ")

    # Security Terminal
    if choice == "1":
        print()
        print("========== SECURITY TERMINAL ==========")

        if not has_keycard:
            print("ACCESS DENIED!")
            print("Level 2 security keycard required.")
            print("You must locate a keycard before accessing the terminal.")
            print("Returning to the main hallway.")

        elif terminal_restored:
            print("The security terminal has already been restored.")
            print("No additional repairs are required.")

        else:
            print("Security keycard detected.")
            print("ACCESS GRANTED!")
            print()
            print("You begin restoring the damaged security network.")
            print("The security alert decreases by 5.")
            print("The repair takes 10 minutes.")

            security_level = max(0, security_level - 5)
            time_remaining = time_remaining - 10
            terminal_restored = True

            print()
            print("Security terminal successfully restored!")
            print(f"Security Alert: {security_level}/100")
            print(f"Time Remaining: {time_remaining} minutes")

    # Storage Room
    elif choice == "2":
        print()
        print("========== STORAGE ROOM ==========")
        print("You enter a dimly lit storage room.")
        print("Three lockers are positioned along the wall.")
        print("Each locker may contain useful equipment.")

        in_storage = True

        while in_storage and time_remaining > 0:

            print()
            print("========== STORAGE ROOM OPTIONS ==========")
            print("1. Search Locker A - Security Equipment")
            print("2. Search Locker B - Medical Supplies")
            print("3. Search Locker C - Maintenance Equipment")
            print("4. Return to Main Hallway")
            print()

            storage_choice = input("Choose an option (1-4): ")

            # Locker A - Security Keycard
            if storage_choice == "1":
                print()
                print("========== LOCKER A ==========")

                if has_keycard:
                    print("You already collected the security keycard.")
                    print("There is nothing else useful inside.")

                else:
                    print("You open Locker A.")
                    print("Inside, you discover a Level 2 security keycard!")
                    print("This keycard can unlock the security terminal.")

                    has_keycard = True
                    time_remaining = time_remaining - 5

                    print()
                    print("Security Keycard Acquired!")
                    print(f"Time Remaining: {time_remaining} minutes")

            # Locker B - Medical Kit
            elif storage_choice == "2":
                print()
                print("========== LOCKER B ==========")

                if has_medkit:
                    print("You already collected the medical kit.")
                    print("There are no additional medical supplies.")

                else:
                    print("You search through the medical locker.")
                    print("You discover an emergency medical kit.")
                    print("The kit can restore health later.")

                    has_medkit = True
                    time_remaining = time_remaining - 5

                    print()
                    print("Medical Kit Acquired!")
                    print(f"Time Remaining: {time_remaining} minutes")

            # Locker C - Repair Tools
            elif storage_choice == "3":
                print()
                print("========== LOCKER C ==========")

                if has_tools:
                    print("You already collected the repair tools.")
                    print("There is nothing else useful inside.")

                else:
                    print("You open the maintenance locker.")
                    print("Inside, you find a set of repair tools.")
                    print("These tools may help restore damaged systems.")

                    has_tools = True
                    time_remaining = time_remaining - 5

                    print()
                    print("Repair Tools Acquired!")
                    print(f"Time Remaining: {time_remaining} minutes")

            # Return to Hallway
            elif storage_choice == "4":
                print()
                print("You leave the storage room.")
                print("Returning to the main security hallway.")

                in_storage = False

            else:
                print()
                print("Invalid choice. Please select 1, 2, 3, or 4.")

    # View Player Status
    elif choice == "3":
        print()
        print("========== CURRENT PLAYER STATUS ==========")
        print(f"Player: {player_name}")
        print(f"Health: {health}")
        print(f"Security Alert: {security_level}/100")
        print(f"Time Remaining: {time_remaining} minutes")
        print(f"System Integrity: {system_integrity}%")

        print()
        print("========== INVENTORY ==========")
        print(f"Security Keycard: {has_keycard}")
        print(f"Medical Kit: {has_medkit}")
        print(f"Repair Tools: {has_tools}")
        print(f"Security Terminal Restored: {terminal_restored}")

    # End Exploration
    elif choice == "4":
        print()
        print("You decide to end your current investigation.")
        exploring = False

    else:
        print()
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# End of Game
print()
print("========== MISSION STATUS ==========")

if time_remaining <= 0:
    print("LOCKDOWN COMPLETE!")
    print("The facility has entered permanent lockdown.")
    print("You failed to escape before time expired.")

elif security_level >= 100:
    print("SECURITY ALERT CRITICAL!")
    print("The facility's automated defenses have taken control.")
    print("Mission failed.")

elif terminal_restored:
    print("You successfully restored the security terminal.")
    print("However, the main network and emergency exit remain offline.")
    print("Your investigation will continue in future updates.")

else:
    print("You ended your investigation before restoring the network.")

print()
print("========== FINAL PLAYER STATUS ==========")
print(f"Player: {player_name}")
print(f"Health: {health}")
print(f"Security Alert: {security_level}/100")
print(f"Time Remaining: {max(0, time_remaining)} minutes")
print(f"Security Keycard: {has_keycard}")
print(f"Medical Kit: {has_medkit}")
print(f"Repair Tools: {has_tools}")
print(f"Security Terminal Restored: {terminal_restored}")

print()
print("========== END OF PROTOTYPE ==========")
print(f"Thank you for playing Dead Signal, {player_name}.")
