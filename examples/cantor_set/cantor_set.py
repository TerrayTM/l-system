from l_system import LSystem

seed = "F"

rules = {
  "F": "F+F-F-F+F"
}

def _F(t, p, a):
  t.forward(8)

def _plus(t, p, a):
  t.left(90)

def _minus(t, p, a):
  t.right(90)

definitions = {
  "F": _F,
  "+": _plus,
  "-": _minus
}

l_system = LSystem(seed, rules, definitions)
l_system.compute(4)
l_system.draw()