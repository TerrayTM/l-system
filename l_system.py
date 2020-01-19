import turtle

class LSystem:
  def __init__(self, seed, rules, definitions, initial_x=0, initial_y=0, initial_angle=0, speed=0):
    self._initial_x = initial_x
    self._initial_y = initial_y
    self._initial_angle = initial_angle
    self._seed = seed
    self._state = seed
    self._rules = rules
    self._definitions = definitions
    self._turtle = turtle.Turtle()
    self._turtle.penup()
    self._turtle.goto(initial_x, initial_y)
    self._turtle.pendown()
    self._turtle.setheading(initial_angle)
    self._turtle.speed(speed)

    keys = definitions.keys()
      
    for key in keys:
      if not isinstance(key, str) or not len(key) == 1:
        raise TypeError()
      
    keys = rules.keys()
    
    for key in keys:
      if not isinstance(key, str) or not len(key) == 1:
        raise TypeError()



  def compute(self, depth):
    if depth <= 0:
      return

    nextState = ""

    for i in range(len(self._state)):
      current = self._state[i]

      if current in self._rules:
        nextState += self._rules[current]
      else:
        nextState += self._state[i]
    
    self._state = nextState

    self.compute(depth - 1)



  def reset(self, reset_state=True):
    if reset_state:
      self._state = self._seed
    
    self._turtle.penup()
    self._turtle.goto(self._initial_x, self._initial_y)
    self._turtle.pendown()
    self._turtle.setheading(self._initial_angle)



  def draw(self):
    positions = []
    angles = []

    for i in range(len(self._state)):
      current = self._state[i]

      if current in self._definitions:
        self._definitions[current](self._turtle, positions, angles)

    self.reset(False)
