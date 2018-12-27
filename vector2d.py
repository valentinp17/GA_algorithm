from math import sqrt, acos


def normalize(vector):
    v_sum = vector.x + vector.y
    return Vector2D(vector.x / v_sum, vector.y / v_sum)


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

    def __repr__(self):
        return f'Vector2D({self.x}, {self.y})'

    def __mul__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vector2D(self * other.x, self * other.y)
        elif isinstance(other, types):
            return Vector2D(self.x * other, self.y * other)
        else:
            return Vector2D(self.x * other.x, self.y * other.y)

    def __copy__(self):
        return Vector2D(self.x, self.y)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def get_norm_direction_to(self, vector):
        dist = self.distance(vector)
        return Vector2D((vector.x - self.x) / dist, (vector.y - self.y) / dist)

    def get_direction_to(self, vector):
        return Vector2D((vector.x - self.x), (vector.y - self.y))
