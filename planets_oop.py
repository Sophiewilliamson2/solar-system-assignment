# DISCLAIMER: This code was assisted by ChatGPT
"""
This program is a simple, class-based Solar System info program.
- Demonstrates OOP with Planet and SolarSystem classes based on learning over the last 7 weeks
- Includes appropriate data structures including a separate dictionary for planets and a list for moons
- A simple CLI (Command Line Interface) menu has been created
- Input validation has been implmented
- File I/O is used to load planet data from a JSON file with error handling
- Free text Q&A for four common queries about planets (mass, all facts, moon count, existence)
"""

from typing import List, Dict, Optional
import json
from pathlib import Path

class Planet:
    """Represents one planet with basic facts."""
    def __init__(self, name: str, mass_kg: float, distance_au: float, moons: List[str]) -> None:
        self.name = name
        self.mass_kg = mass_kg
        self.distance_au = distance_au
        self.moons = moons  # list of strings

    def summary(self) -> str:
        """Return a readable multi-line description."""
        moons_str = ", ".join(self.moons) if self.moons else "No listed moons"
        return (
            f"Name: {self.name}\n"
            f"Mass: {self.mass_kg:.3e} kg\n"
            f"Distance from Sun: {self.distance_au} AU\n"
            f"Moons ({len(self.moons)}): {moons_str}"
        )


class SolarSystem:
    """Holds planets and provides simple queries."""
    def __init__(self, planets: List[Planet]) -> None:
        # dict for fast case-insensitive lookup
        self._by_name: Dict[str, Planet] = {p.name.lower(): p for p in planets}

    def has(self, name: str) -> bool:
        return name.lower() in self._by_name

    def get(self, name: str) -> Optional[Planet]:
        return self._by_name.get(name.lower())

    def names_in_order(self) -> List[str]:
        # Keep the canonical eight planets in a friendly order
        order = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
        return [n for n in order if n.lower() in self._by_name]
    
    def all_names_lower(self) -> List[str]:
        return list(self._by_name.keys()) 


# This section will now load planets from a JSON file and apply basic validation to highlight 
# if the file did not exist or had invalid data. This demonstrates file I/O and error handling using try/except blocks.

def build_default_system() -> SolarSystem:
    """Load planets from planets.json (This is located in the same folder) with simple validation."""
    json_path = Path(__file__).parent / "planets.json"
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            rows = json.load(f) # may raise JSONDecodeError
    except FileNotFoundError:
        print("Could not find planets.json. Starting with an empty Solar System.")
        return SolarSystem([]) 
    except json.JSONDecodeError as e:
        print("Invalid JSON in planets.json:", e)
        return SolarSystem([]) 

    planets: List[Planet] = []
    for i, row in enumerate(rows, start=1):
        try:
            planets.append(
                Planet(
                    name=row["name"],
                    mass_kg=float(row["mass_kg"]),
                    distance_au=float(row["distance_au"]),
                    moons=list(row.get("moons", [])),
                )
            )
        except (KeyError, TypeError, ValueError) as e:
            print(f"Skipping row {i}: {e}")
            continue

    return SolarSystem(planets)


# This setion defines a simple free-text Q&A function that can answer four common types of questions about planets.

def _find_planet_name_in_text(system: SolarSystem, text: str) -> Optional[str]:
    """Return the first known planet mentioned in text (case-insensitive), or None."""
    t = text.lower()
    for name in system.all_names_lower() + ["pluto"]:  # allow 'pluto' queries, even if not in JSON
        if name in t:
            return name
    return None


def answer_question(system: SolarSystem, q: str) -> None:
    """
    Very simple keyword-based Q&A for four intents:
    - 'Tell me everything about Saturn'
    - 'How massive is Neptune?'
    - 'Is Pluto in the list of planets?'
    - 'How many moons does Earth have?'
    """
    q_low = q.strip().lower()
    if not q_low:
        print("Please enter a non-empty question.")
        return

    pname = _find_planet_name_in_text(system, q_low)

    # 1) "Tell me everything about X"
    if pname and ("tell me everything" in q_low or "about" in q_low or "info" in q_low):
        p = system.get(pname)
        if p:
            print(p.summary())
        else:
            print(f"{pname.title()} is not in the list of planets.")
        return

    # 2) "How massive is X?"
    if pname and ("how massive" in q_low or "mass" in q_low):
        p = system.get(pname)
        if p:
            print(f"{p.name} has a mass of {p.mass_kg:.3e} kg.")
        else:
            print(f"{pname.title()} is not in the list of planets.")
        return

    # 3) "Is X in the list of planets?"
    if pname and (" in the list" in q_low or q_low.startswith("is ") or " is " in q_low):
        print("Yes." if system.has(pname) else "No.")
        return

    # 4) "How many moons does X have?"
    if pname and ("how many" in q_low and "moon" in q_low):
        p = system.get(pname)
        if p:
            n = len(p.moons)
            print(f"{p.name} has {n} {'moon' if n == 1 else 'moons'}.")
        else:
            print(f"{pname.title()} is not in the list of planets.")
        return

    # Fallback guidance
    print("Sorry, I don't understand that question.  I can answer things like:\n"
          "- Tell me everything about Saturn\n"
          "- How massive is Neptune?\n"
          "- Is Pluto in the list of planets?\n"
          "- How many moons does Earth have?")




# The following section implements a simple CLI menu to interact with the SolarSystem class.

def menu() -> None:
    print("\nThis is a a Solar System Program ")
    print("\nWe have lots of planets on our list. What would you like to do?")
    print("\n")
    print("1) I can tell you lots of interesting facts about a particular planet")
    print("2) Do you want to know the just the mass of a planet?")
    print("3) Want to check if your planet is on our list?")
    print("4) How many moons does a particular planet have?")
    print("5) List all planet in this program")
    print("6) Ask a free-text question about a planet (eg. 'How massive is Jupiter?' or 'Tell me everything about Mars')")
    print("7) Quit the program")

def ask_name(prompt: str) -> str:
    name = input(prompt).strip()
    return name

def main() -> None:
    system = build_default_system()
    print("Welcome! Let's get started")

    while True:
        menu()
        choice = input("Choose (1-7): ").strip()

        if choice == "1":
            name = ask_name("Type in which planet you are interested in: ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            p = system.get(name)
            if p:
                print("\n" + p.summary())
            else:
                print(f"Unfortunately {name} is not currently on our list of planets.")

        elif choice == "2":
            name = ask_name("Type in which planet do you want to know the mass of: ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            p = system.get(name)
            if p:
                print(f"{p.name} has a mass of {p.mass_kg:.3e} kg. That's massive!")
            else:
                print(f" Unfortunately {name} is not currently on our list of planets.")

        elif choice == "3":
            name = ask_name("Type in which planet you are interested in: ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            print("Yes, this planet is on our list" if system.has(name) else "No, sorry this planet is not currently on our list.")

        elif choice == "4":
            name = ask_name("Type in which planet you are interested in: ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            p = system.get(name)
            if p:
                count = len(p.moons)
                label = "moon" if count == 1 else "moons"
                print(f"{p.name} has {count} {label}.")
            else:
                print(f"{name} is not in the list of planets.")

        elif choice == "5":
            print("\nPlanets we have in our list:")
            for n in system.names_in_order():
                print(f"- {n}")

        elif choice == "6":
            q = input("Ask your question: ")
            answer_question(system, q)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("This is an invalid choice. Please try again and enter 1, 2, 3, 4, 5, 6 or 7.")


if __name__ == "__main__":
    main()
