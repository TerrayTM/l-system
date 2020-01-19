from l_system import LSystem

seed = "F"

rules = {
  "F": "FF+[+F-F-F]-[-F+F+F]"
}

def _F(t, p, a):
  t.forward(8)

def _plus(t, p, a):
  t.right(22.5)

def _minus(t, p, a):
  t.left(22.5)

def _leftBracket(t, p, a):
  p.append(t.pos())
  a.append(t.heading())

def _rightBracket(t, p, a):
  x, y = p.pop()
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.setheading(a.pop())

definitions = {
  "F": _F,
  "[": _leftBracket,
  "]": _rightBracket,
  "-": _minus,
  "+": _plus
}

l_system = LSystem(seed, rules, definitions, initial_angle=90)
l_system.compute(6)
l_system.draw()