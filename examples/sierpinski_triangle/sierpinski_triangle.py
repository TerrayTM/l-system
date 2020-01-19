from l_system import LSystem

seed = "F-G-G"

rules = {
  "F": "F-G+F+G-F",
  "G": "GG"
}

def _F(t, p, a):
  t.forward(8)

def _G(t, p, a):
  t.forward(8)

def _plus(t, p, a):
  t.left(120)

def _minus(t, p, a):
  t.right(120)

definitions = {
  "F": _F,
  "G": _G,
  "-": _minus,
  "+": _plus
}

l_system = LSystem(seed, rules, definitions, initial_angle=90)
l_system.compute(6)
l_system.draw()