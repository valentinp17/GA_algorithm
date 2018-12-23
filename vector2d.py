from math import sqrt


def normalize(vector):
    return [float(i)/sum(vector) for i in vector]


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'Vector2D({self.x}, {self.y})'

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

