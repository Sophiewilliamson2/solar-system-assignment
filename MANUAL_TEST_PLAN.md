
Test Plan — Solar System Program

Purpose and scope
- The scope of this test to is verify that the program loads without errors
- Planet data is loaded from separate dictionary file planet.json and supports the 6 menu items which are
1) I can tell you lots of interesting facts about a particular planet
2) Do you want to know the just the mass of a planet?
3) Want to check if your planet is on our list?
4) How many moons does a particular planet have?
5) List all planet in this program
6) Ask a free-text question about a planet (eg. 'How massive is Jupiter?' or 'Tell me everything about Mars')
7) Quit the program
- The test plan is to
- verify class behaviours
- Data correctness
- Menu flows
- Input validation.

Test Environment
- Python (version 3)
- Command to be run from terminal python3 planets_oop.py
- Files required:
- planets_oop.py 
- planets.json (this MUST be stored in the same folder as planets_oop.py)

Assumptions
- planets.json has objects with keys: name, mass_kg, distance_au, moons (list)

Test Cases (TC)

[TC-1] Start & menu
1. Start program
Steps: Run python planets_oop.py
Expected result: Welcome message and menu options 1–7 displayed.  

2. Invalid menu choice
Steps: Enter X or 9
Expected "This is an invalid choice. Please try again and enter 1, 2, 3, 4, 5, 6 or 7."

3. Check Dictionary data loading (JSON)
Steps: Run program and choose option 5
Expected result: Lists all planets in order in planets.json dictionary file.  This should be 8 planet names.
Planets we have in our list:
- Mercury
- Venus
- Earth
- Mars
- Jupiter
- Saturn
- Uranus
- Neptune

[TC-2] Menu items 1-5

Menu item 1) I can tell you lots of interesting facts about a particular planet
Steps: From menu choose 1 → enter "Saturn"
Expected result: Multi-line summary:-
Name: Saturn
Mass: 5.683e+26 kg
Distance from Sun: 9.537 AU
Moons (4): Titan, Enceladus, Rhea, Mimas

Menu item 2) Do you want to know the just the mass of a planet?
Steps: From menu choose 2 → enter "Jupiter"
Expected result: Jupiter has a mass of 1.898e+27 kg. That's massive!

Menu item 3) Want to check if your planet is on our list?
Steps: From menu choose 3 → enter "Earth"
Expected result: Yes, this planet is on our list

Menu item 4) How many moons does a particular planet have?
Steps: From menu choose 4 → enter "Saturn"
Expected result: Saturn has 4 moons.

Menu item 5) List all planet in this program
Steps: From menu choose 5
Expected result: Lists all planets in order as per planets.json dictionary file.  This should be 8 planet names.
Planets we have in our list:
- Mercury
- Venus
- Earth
- Mars
- Jupiter
- Saturn
- Uranus
- Neptune

[TC-2] Menu items 6 Free text questions and answers

Q1: Ask a free-text question about a planet
Ask everything about a planet
Steps: type Tell me everything about Saturn
Expected result: 
Name: Saturn
Mass: 5.683e+26 kg
Distance from Sun: 9.537 AU
Moons (4): Titan, Enceladus, Rhea, Mimas

Q2: 

[TC-3] Mass of Neptune
- Choose 2 → enter "Neptune"
- Expect "Neptune has a mass of ..." in scientific notation.

[TC-4] Is Pluto in the list?
- Choose 3 → enter "Pluto"
- Expect "No."

[TC-5] Moons of Earth
- Choose 4 → enter "Earth"
- Expect "Earth has 1 moon."

[TC-6] List all planet names
- Choose 5
- Expect eight names in order Mercury → Neptune.

[TC-7] Unknown name
- Choose 1 (or 2/4) → enter "Ceres"
- Expect "Ceres is not in the list of planets."

[TC-8] Empty input validation
- Choose 2 → press Enter
- Expect "Please enter a non-empty name."

[TC-9] Case-insensitive lookup
- Choose 4 → enter "eArTh"
- Expect the same result as "Earth".

Exit Criteria
- All menu options work without unhandled exceptions
- Data correctly loads from JSON: if file missing a warning is given and the program continues gracefully
- Free text question / answer works correctly
- Case insensitive planet look up succeeds
- Clear error messages are shown for planets not on our list, invalid or empty input
