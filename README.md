
# Dead Signal

## Project Description

Dead Signal is a text-based cybersecurity adventure and survival game developed in Python for MS539.

The game takes place in the year 2042 inside a classified underground research facility. A major network failure has triggered an emergency lockdown, trapping the player inside.

The player takes the role of a cybersecurity specialist who must investigate the facility, collect equipment, restore compromised security systems, and eventually escape before the facility enters permanent lockdown.

Players must make decisions that affect their available resources, inventory, and progress throughout the game.

## Development Track

Core Developer Track

This project focuses on creating a command-line adventure and survival game using fundamental Python programming concepts.

## Current Features

The current prototype includes:

- Game introduction explaining the setting and objective.
- Player name input and personalized welcome message.
- Player health tracking.
- Facility security alert level.
- Lockdown countdown timer.
- System integrity tracking.
- Main hallway with multiple player decisions.
- Storage room containing three searchable lockers.
- Security keycard required to access the security terminal.
- Medical kit and repair tools that can be collected.
- Inventory tracking using Boolean variables.
- Resource calculations that update remaining time and security alerts.
- Navigation between the main hallway and storage room.
- Prevention of duplicate item collection.
- Security terminal restoration.
- Invalid menu choice handling.
- Game-ending conditions and final player status.

## Gameplay

The player begins inside the facility's main security hallway.

From the hallway, the player can:

1. Access the security terminal.
2. Enter the storage room.
3. View player status and inventory.
4. End exploration.

### Security Terminal

The security terminal requires a Level 2 security keycard.

Without the keycard, access is denied.

After obtaining the keycard, the player can access the terminal and restore limited security functionality.

Restoring the terminal decreases the security alert level but consumes additional time.

### Storage Room

The storage room contains three lockers:

**Locker A - Security Equipment**
- Contains a Level 2 security keycard.
- Allows access to the security terminal.

**Locker B - Medical Supplies**
- Contains an emergency medical kit.
- Will be used to restore health in future updates.

**Locker C - Maintenance Equipment**
- Contains repair tools.
- Will be used to repair damaged facility systems in future updates.

Searching a locker consumes five minutes.

Items can only be collected once.

### Player Resources

The game tracks the following resources:

- Health: Starts at 100.
- Security Alert: Starts at 10 out of 100.
- Time Remaining: Starts at 60 minutes.
- System Integrity: Starts at 75.5%.
- Security Keycard: Initially unavailable.
- Medical Kit: Initially unavailable.
- Repair Tools: Initially unavailable.

An initial facility event increases the security alert and decreases the remaining time.

Player decisions can cause additional changes.

## Win and Lose Conditions

### Planned Win Condition

The player will eventually win by restoring the main security network, disabling the hostile program, and escaping the facility.

The complete win condition has not yet been implemented.

### Current Lose Conditions

The player fails if:

- The lockdown timer reaches zero.
- The facility security alert reaches 100.

The player can also voluntarily end exploration.

## Running the Program

### Requirements

- Python 3
- Visual Studio Code or another code editor

### Instructions

1. Download or clone the project repository.
2. Open the DeadSignal folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run the following command:

    python main.py

5. Follow the instructions displayed in the terminal.

On some Windows installations, the program may be started using:

    py main.py

No additional Python libraries are currently required.

## Project Structure

DeadSignal/
    main.py
    README.md

### main.py

Contains the game's introduction, player information, resource variables, decision-making logic, inventory tracking, and gameplay menus.

### README.md

Contains the project description, setup instructions, current features, and planned development.

## Planned Development

Future milestones may introduce:

1. Additional rooms and facility exploration.
2. Functional medical kits that restore health.
3. Repair tools that improve system integrity.
4. Security and logic puzzles.
5. Environmental hazards and damage.
6. More advanced inventory management.
7. Additional security clearance levels.
8. Functions to organize repeated game operations.
9. Classes to represent players, rooms, and equipment.
10. Saving and loading game progress.
11. Automated testing and error handling.
12. Multiple endings and a complete escape objective.

## Development Tools

- Python 3
- Visual Studio Code
- Git
- GitHub

## Course Information

Course: MS539

Development Track: Core Developer Track

Project Type: Python Command-Line Adventure / Survival Game

## Project Status

Initial functional prototype developed.

The current version demonstrates player input, variables, multiple data types, calculations, conditional statements, loops, inventory tracking, and meaningful player decisions.

Additional gameplay systems and the complete win condition will be developed in future milestones.
