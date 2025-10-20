
Test Plan — Solar System Program

Purpose and scope
- The scope of this test to is verify that the program starts without unhandled exceptions or errors
- Verity planet data is loaded from separate JSON file (planet.json) and supports menu options 1-7 (listed)
1) I can tell you lots of interesting facts about a particular planet
2) Do you want to know the just the mass of a planet?
3) Want to check if your planet is on our list?
4) How many moons does a particular planet have?
5) List all planet in this program
6) Ask a free-text question about a planet (eg. 'How massive is Jupiter?' or 'Tell me everything about Mars')
7) Quit the program

The test plan is to
- Verify class behaviours
- Data correctness
- Menu flows
- Input validation
- Free text questions and answers

Test Environment
- Python (version 3.x)
- Command to be run from terminal python3 planets_oop.py
- Files required:
- planets_oop.py 
- planets.json (this MUST be stored in the same folder as planets_oop.py)

Assumptions
- Each JSON row listed has: name, mass_kg, distance_au, moons (list)

Test Cases (TC)

TC-1 Start
1. Start program
Steps: Run python planets_oop.py
Expected result: Welcome message and menu options 1–7 displayed. No traceback

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

TC-2 Menu items 1-5

Menu item 1) I can tell you lots of interesting facts about a particular planet
Steps: From menu choose 1 → enter "Saturn"
Expected result: 
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

TC-3 Menu items 6 Free text questions and answers

Q1: Ask a free-text question to ask for all information stored about a planet
Steps: type "Tell me everything you have stored about Saturn"
Expected result: Name: Saturn
Mass: 5.683e+26 kg
Distance from Sun: 9.537 AU
Moons (4): Titan, Enceladus, Rhea, Mimas

Q2: Ask a free-text question to find out the mass of a planet
Steps: type "How massive is Neptune?"
Expected result: Neptune has a mass of 1.024e+26 kg.

Q3: Ask a free-text question to see if a planet is in the list
Steps: type "Is pluto in your planet list?"
Expected result: No (as Pluto is not in the dictionary list of planets)

Q5: Ask a free-text question to find out how many moons a particular planet has
Steps: type "How many moons does Jupiter have?"
Expected result: Jupiter has 4 moons.

Q6: Ask a free-text question about a planet which is not in the planet dictionary/list
Steps: type "Tell me everything about planet Clingon"
Expected result: Sorry, I don't understand that question.  I can answer things like:
Tell me everything about Saturn
How massive is Neptune?
Is Pluto in the list of planets?
How many moons does Earth have?

TC-4 verify data input and data handling

Q1. Case insensitive planet lookup
Steps: From menu choose 2 → enter "JuPiTer"
Expected result: Jupiter has a mass of 1.898e+27 kg. That's massive!

Q2: Handling empty input
Steps: Steps: From menu choose 2 → enter 
Expected result: Please enter a non-empty name.

Exit Criteria
- All menu options work without unhandled exceptions
- Data correctly loads from JSON or fails gracefully with clear message
- Free text question / answer works correctly
- Case insensitive planet look up succeeds
- Clear error messages are shown for planets not on our list, invalid or empty input
