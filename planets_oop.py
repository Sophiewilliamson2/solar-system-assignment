# DISCLAIMER: This code was assisted by ChatGPT
"""
This program displays simple information about planets in our solar system.  
It demonstrates the learning from the last 7 weeks including:
- OOP - Object-orientated programming (Planet, SolarSystem)
- Classes have been used throughout the program
- Appropriate data structures (dictionary for planets, list for moons)
- A simple menu has been provided
- User input is validated
- No files / DB / web
"""

from typing import List, Dict, Optional

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


def build_default_system() -> SolarSystem:
    """Create a SolarSystem with basic data (values approx.)."""
    data = [
        Planet("Mercury", 3.3011e23, 0.387, []),
        Planet("Venus",   4.8675e24, 0.723, []),
        Planet("Earth",   5.97237e24, 1.0,   ["Moon"]),
        Planet("Mars",    6.4171e23,  1.524, ["Phobos", "Deimos"]),
        Planet("Jupiter", 1.8982e27,  5.203, ["Io", "Europa", "Ganymede", "Callisto"]),
        Planet("Saturn",  5.6834e26,  9.537, ["Titan", "Enceladus", "Rhea", "Mimas"]),
        Planet("Uranus",  8.6810e25, 19.191, ["Titania", "Oberon", "Umbriel", "Ariel"]),
        Planet("Neptune", 1.02413e26, 30.07, ["Triton", "Nereid"]),
    ]
    return SolarSystem(data)


# User Input Menu

def menu() -> None:
    print("\nSolar System")
    print("1) Tell me everything about a planet")
    print("2) What is the size of a specific planet?")
    print("3) Is a name in the list of planets?")
    print("4) How many moons does a planet have?")
    print("5) List all planet names")
    print("6) Quit")

def ask_name(prompt: str) -> str:
    name = input(prompt).strip()
    return name

def main() -> None:
    system = build_default_system()
    print("Welcome! (Class-based version)")

    while True:
        menu()
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            name = ask_name("Enter a planet name (e.g., Saturn): ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            p = system.get(name)
            if p:
                print("\n" + p.summary())
            else:
                print(f"{name} is not in the list of planets.")

        elif choice == "2":
            name = ask_name("Enter a planet name (e.g., Neptune): ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            p = system.get(name)
            if p:
                print(f"{p.name} has a mass of {p.mass_kg:.3e} kg.")
            else:
                print(f"{name} is not in the list of planets.")

        elif choice == "3":
            name = ask_name("Enter a name to check (e.g., Pluto): ")
            if not name:
                print("Please enter a non-empty name.")
                continue
            print("Yes." if system.has(name) else "No.")

        elif choice == "4":
            name = ask_name("Enter a planet name (e.g., Earth): ")
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
            print("\nPlanets:")
            for n in system.names_in_order():
                print(f"- {n}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
