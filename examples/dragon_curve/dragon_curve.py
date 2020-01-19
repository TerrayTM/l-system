from l_system import LSystem

seed = "FX"

rules = {
  "X": "X+YF+",
  "Y": "-FX-Y"
}

def _F(t, p, a):
  t.forward(8)

def _plus(t, p, a):
  t.right(90)

def _minus(t, p, a):
  t.left(90)

definitions = {
  "F": _F,
  "-": _minus,
  "+": _plus
}

l_system = LSystem(seed, rules, definitions, initial_angle=90)
l_system.compute(12)
l_system.draw()