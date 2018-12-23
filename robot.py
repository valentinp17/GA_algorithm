from vector2d import Vector2D


class Robot:
    def __init__(self):
        self.position = Vector2D(0, 0)
        self.velocity = Vector2D(0, 0)

    def distance(self, other):
        return self.position.distance(other.position)

    def __repr__(self):
        return f'Robot(pos={self.position.x, self.position.y},' \
               f' vel={self.velocity.x, self.velocity.y})'