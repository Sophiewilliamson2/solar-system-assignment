DISCLAIMER: This test plan was assisted by ChatGPT

Test Plan — Solar System (OOP Beginner Version)

Scope
- Verify class behaviours, data correctness, menu flows, and input validation.

Items
- planets_oop.py (Planet, SolarSystem, CLI)

Test Cases

[TC-1] Start & menu
- Run program → menu options 1–6 displayed.

[TC-2] Everything about Saturn
- Choose 1 → enter "Saturn"
- Expect multi-line summary with name, mass (~5.6834e26 kg), distance (~9.537 AU), and listed moons.

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
- All test cases behave as expected.
