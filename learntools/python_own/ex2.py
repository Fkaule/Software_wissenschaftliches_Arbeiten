from learntools.core import *
from learntools.core.problem import injected

class Flaechentraegheitsmoment(EqualityCheckProblem):
    _vars = ['I']
    _expected = [(30*30**3)/12]

    _hint = "Syntax für Potenz ist:  `a ** b`"
    _solution = CS('I = (b*h**3)/12')


qvars = bind_exercises(globals(), [
    Flaechentraegheitsmoment,
    ],
    start=0,
    )
__all__ = list(qvars)
