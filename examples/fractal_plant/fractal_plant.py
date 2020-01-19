from l_system import LSystem

seed = "X"

rules = {
  "X": "F+[[X]-X]-F[-FX]+X",
  "F": "FF"
}

def _F(t, p, a):
  t.forward(6)

def _leftBracket(t, p, a):
  p.append(t.pos())
  a.append(t.heading())

def _rightBracket(t, p, a):
  x, y = p.pop()
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.setheading(a.pop())

def _plus(t, p, a):
  t.right(25)

def _minus(t, p, a):
  t.left(25)

definitions = {
  "F": _F,
  "[": _leftBracket,
  "]": _rightBracket,
  "-": _minus,
  "+": _plus
}

l_system = LSystem(seed, rules, definitions, initial_angle=60)
l_system.compute(6)
l_system.draw()