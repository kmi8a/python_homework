import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance (other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented
    
    def __str__(self):
        return f"x:{self.x}, y:{self.y}"
    
    def __repr__(self):
        return f'point(x={self.x}, y={self.y})'
    
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"x:{self.x}, y:{self.y}, distance:{self.length:.2f}"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    @property
    def length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
    
point1 = Point(5, 15)
point2 = Point(1, 15)
euclidian = point1.distance_to(point2)

print(point1)
print(point1 == point2)
print(euclidian)

vector1 = Vector(1, 16)
vector2 = Vector(3, 8)

print(vector1)

print(vector1 + vector2)