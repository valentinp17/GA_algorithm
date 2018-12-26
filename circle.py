from vector2d import Vector2D


class Circle:
    def __init__(self, x, y, r):
        self.position = Vector2D(x, y)
        self.radius = r

    def __str__(self):
        return f'Circle({self.position.x}, {self.position.y}, {self.radius})'

    def __repr__(self):
        return f'Circle({self.position.x}, {self.position.y}, {self.radius})'
