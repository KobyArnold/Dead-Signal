
#
# Dead Signal

**Course:** MS539
**Development Track:** Core Developer Track

## Project Description

Dead Signal is a Python command-line cybersecurity survival adventure
set in an underground research facility in the year 2042.

The player must collect a Level 2 security keycard and repair tools,
restore the security terminal and main network, and escape before
permanent lockdown.

## Project Files

- main.py - Game introduction, main loop, and ending.
- player.py - Player resources, inventory, and mission outcomes.
- world.py - Locations, decisions, input validation, and random events.
- README.md - Project documentation.

## Running the Game

1. Install Python 3.
2. Open the DeadSignal folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run:

    python main.py

On Windows, you may also use:

    py main.py

No third-party Python packages are required.

## Current Features

- Player name and starting resources
- Health, security alert, time, and system integrity
- Multiple locations and navigation menus
- Three searchable storage lockers
- Inventory management
- Security keycard requirement
- Repair tools and network restoration
- Usable medical kits
- Random environmental hazards
- Meaningful player decisions
- Input validation
- Win and lose conditions
- Functions with parameters and return values
- Type hints and docstrings
- Three Python modules

## Win Condition

Restore the security terminal, repair the main network,
and escape through the emergency exit.

## Lose Conditions

The player loses when:

- Health reaches zero.
- Security alert reaches 100.
- Remaining time reaches zero.

## Debugging in Visual Studio Code

1. Open world.py.
2. Set a breakpoint inside search_locker().
3. Start debugging with F5.
4. Enter the storage room and select a locker.
5. Inspect the player, locker, and item variables.
6. Use Step Over to observe resource changes.
7. Use Step Into to inspect collect_item().
8. Search the same locker again to verify duplicate prevention.

## Debugging Report

Problem Observed:
[Describe an actual issue encountered.]

How It Was Identified:
[Explain the breakpoints and debugger tools used.]

Correction:
[Explain the correction and how it was tested.]

## Planned Development

Future milestones may include:

- Additional facility locations
- More environmental hazards
- Security puzzles
- Expanded inventory systems
- Save and load functionality
- Automated tests
- Additional story endings

## Project Status

Checkpoint 3: Functions and Modules

Development Track: Core Developer Track

