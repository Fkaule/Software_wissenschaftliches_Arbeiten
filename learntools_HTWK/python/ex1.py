from learntools.core import *
from learntools.core.problem import injected

class Flaechentraegheitsmoment(EqualityCheckProblem):
    _vars = ['I']
    _expected = [(30*30**3)/12]

    _hint = "Syntax für Potenz ist:  `a ** b`"
    _solution = CS('I = (b*h**3)/12')


class Durchbiegung(EqualityCheckProblem):
    _vars = ['umax']
    _expected = [(5*1000.0*1000.0**3)/(384*200000.0*67500.0)]

    _hint = "Syntax für Potenz ist:  `a ** b`"
    _solution = CS('umax = (5*q*L**3)/(384*E*I)')
    
class Durchbiegung2(EqualityCheckProblem):
    _vars = ['umax']
    _expected = [(1000.0*1000.0**3)/(3*70000.0*540000.0)]

    _hint = "Die Höhe hat sich geändert auf h=60mm und dadurch muss das Flächenenträgheitsmoment I neu berechnet werden`"
    _solution = CS('umax=(F*L**3)/(3*E*I)')


qvars = bind_exercises(globals(), [
    Flaechentraegheitsmoment,
    Durchbiegung,
    Durchbiegung2,
    ],
    start=0,
    )
__all__ = list(qvars)
