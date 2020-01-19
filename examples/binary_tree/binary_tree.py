from l_system import LSystem

seed = "0"

rules = {
  "1": "11",
  "0": "1[0]0"
}

def _0(t, p, a):
  t.forward(6)

def _1(t, p, a):
  t.forward(10)

def _leftBracket(t, p, a):
  p.append(t.pos())
  a.append(t.heading())
  t.left(45)

def _rightBracket(t, p, a):
  x, y = p.pop()
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.setheading(a.pop())
  t.right(45)

definitions = {
  "0": _0,
  "1": _1,
  "[": _leftBracket,
  "]": _rightBracket
}

l_system = LSystem(seed, rules, definitions, initial_angle=90)
l_system.compute(6)
l_system.draw()
