from vector2d import Vector2D
import numpy as np

class Robot:
    def __init__(self, x, y):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0, 0)
        self.current_step = 0
        self.is_alive = True
        route = []
        self.fitness = 0

    def reset(self, x, y):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0, 0)
        self.current_step = 0
        self.is_alive = True
        self.fitness = 0

    def add_route(self, route):
        self.route = route.copy()

    def distance(self, other):
        return self.position.distance(other.position)

    def make_step(self, circles):
        if self.is_alive:
            self.position = self.position.add(self.velocity)
            self.velocity = self.velocity.add(self.route[self.current_step])
            self.current_step += 1
            if self.current_step == len(self.route):
                self.current_step -= 10
            if self.check_collisions(circles):
                self.is_alive = False
                self.fitness = self.get_fitness()


    def __copy__(self):
        robot = Robot(self.position.x, self.position.y)
        robot.velocity = self.velocity.__copy__()
        robot.current_step = self.current_step
        robot.is_alive = self.is_alive
        robot.route = self.route[:]
        robot.fitness = self.fitness
        return robot

    def check_collisions(self, circles):
        if self.position.x < 100 or self.position.x > 900 or \
                self.position.y < 100 or self.position.y > 900:
            return True

        for circle in circles:
            if self.position.distance(circle.position) < circle.radius:
                return True
        return False

    def __repr__(self):
        return f'Robot(pos={self.position.x, self.position.y},' \
               f' vel={self.velocity.x, self.velocity.y},' \
               f' fs={self.fitness},' \
               f' cs={self.current_step})'

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / self.get_distance_finish(Vector2D(800, 800))
        return self.fitness

    def get_distance_finish(self, finish):
        return self.position.distance(finish)
