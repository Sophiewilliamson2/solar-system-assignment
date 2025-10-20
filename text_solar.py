# ChatGPT assisted with code
# Run: pip install pytest && pytest -q

import types
from planets_oop import Planet, SolarSystem, answer_question

class TinySystem(SolarSystem):
    def __init__(self):
        planets = [
            Planet("Earth", 5.972e24, 1.0, ["Moon"]),
            Planet("Neptune", 1.024e26, 30.07, ["Triton"]),
        ]
        super().__init__(planets)

def capture(fn, *args):
    """Capture printed output of a function call."""
    import io, sys
    buf, old = io.StringIO(), sys.stdout
    try:
        sys.stdout = buf
        fn(*args)
        return buf.getvalue()
    finally:
        sys.stdout = old

def test_answer_question_mass():
    sys = TinySystem()
    out = capture(answer_question, sys, "How massive is Neptune?")
    assert "1.024" in out and "kg" in out

def test_answer_question_moons():
    sys = TinySystem()
    out = capture(answer_question, sys, "How many moons does Earth have?")
    assert "Earth has 1 moon" in out

def test_answer_question_unknown():
    sys = TinySystem()
    out = capture(answer_question, sys, "Tell me everything about Pluto")
    assert "not in the list of planets" in out
