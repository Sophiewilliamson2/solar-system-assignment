# Solar System Program

This is my Python program demonstrating what I have learned over the last 7 weeks. 
It shows information about planets in the solar system and lets the user ask questions through a simple menu and also has the option for a free style question and answer section where you can ask 4 of the most common types of questions.  
The program provideds  simple, text based infromation about 8 of the planets in our Solar System.  It demonstrates Object Orientated Programming (OOP) principles using Python as the programming languages.
It inlcudes classes, data structures, file handling and basic user interaction via a Command Line Interface (CLI).

## Learning outcomes

This program is the final assessment as part of the AI MSc Module Fundementals of Computing (Week 7)
It demonstrates:
- Use of classes and objects (Planet, SolarSytem)
- File input/output suing a JSON file (planet.json)
- Input validation and exception handling (try/except)
- A simple command line menu system + free text query handling
- Included some of the principles of defensive programming and testing

## Key features

Raw data is held separately in planets.json which is loaded dynamically
Planet information is displayed such as mass, distance and number of moons
Handles invalid input such as incorrect values or empty gracefully
Allows free text queries such as:
"Tell me everything about Saturn?"
"How massive is Neptune?"
"Is Pluto in the list of Planets?"
"How many moons does the Earth have?"
Includes a test plan for manual testing and an automated unit text plan which can be automated by pytest

## Files which make up this program are:
planets_oop.py This is the main program file
planets.json This is the dictionary file containing the raw planet data
MANUAL_TEST_PLAN.md  This is a test plan to be followed for manual Black Box style testing
test_solar.py This is the automated test plan to be used with pytext command

## Installation and setup
Make sure Python 3.x installed
Download all files into the same folder
Run the program using:
python3 planets_oop.py

## Testing
Manual testing
Follow the manual text plan MANUAL_TEST_PLAN.md which details each test step and expected outcome

Automated testing
install pytest
pip3 install pytest
pytest -q


