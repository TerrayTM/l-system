from l_system import LSystem

seed = "F+F+F+F"

rules = {
  "F": "FF+F++F+F"
}

def _F(t, p, a):
  t.forward(6)

def _plus(t, p, a):
  t.right(90)

def _minus(t, p, a):
  t.left(90)

definitions = {
  "F": _F,
  "-": _minus,
  "+": _plus
}

l_system = LSystem(seed, rules, definitions)
l_system.compute(5)
l_system.draw()