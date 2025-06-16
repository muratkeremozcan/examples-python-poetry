import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def reflect(self, axis):
      if axis == "x":
        self.y = -self.y
      elif axis == "y":
        self.x = -self.x
      elif axis == "origin":
        self.x = -self.x
        self.y = -self.y
      else:
        print("Invalid axis")

p = Point(1, 2)
p.reflect("x")
print(p.x, p.y)
p.reflect("y")
print(p.x, p.y)
p.reflect("origin") # set it back to the original point
print(p.x, p.y)

p2 = Point(1, 2)
p2.reflect("z")
