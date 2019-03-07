import random

from src.models.vector2d import Vector2D


class Individual:
    def __init__(self):
        self.position = Vector2D(0, 0)
        self.velocity = Vector2D(0, 0)
        self.route = []
        self.fitness = 0

    def distance(self, other):
        return self.position.distance(other.position)

    def add_step(self, step):
        self.route.append(step)

    def check_collisions(self, circles, prev_position):
        if self.position.x < 0 or self.position.x > 1 or \
                self.position.y < 0 or self.position.y > 1:
            return True

        for circle in circles:
            if self.position.distance(circle.position) < circle.radius:
                return True
            if Vector2D.get_dist_to_line(self.position, prev_position, circle.position) < circle.radius:
                return True
        return False


    def __repr__(self):
        return f'Indiv(pos={self.position.x, self.position.y},' \
               f' vel={self.velocity.x, self.velocity.y},' \
               f' fs={self.fitness},'

    def get_fitness(self, circles):
        if self.fitness == 0:
            count_path = 0
            for step in self.route:
                prev_position = self.position
                self.position = self.position.add(self.velocity)
                self.velocity = self.velocity.add(step)
                if self.check_collisions(circles, prev_position):
                    self.fitness = 1 / (self.position.distance(Vector2D(1, 1))*0.5 + count_path*0.5)
                    return self.fitness

                count_path += step.length()
            self.fitness = 1 / (self.position.distance(Vector2D(1, 1))*0.5 + count_path*0.5)
        return self.fitness

    def get_path(self, circles):
        indiv = Individual()
        new_path = []
        for step in self.route:
            new_path.append(indiv.position)
            prev_position = indiv.position
            indiv.position = indiv.position.add(indiv.velocity)
            indiv.velocity = indiv.velocity.add(step)
            if indiv.check_collisions(circles, prev_position):
                return new_path
        return new_path

    def mutate_change_step(self, max_force):
        rand = random.randint(0, len(self.route) - 1)
        self.route[rand] = self.create_random_step(max_force)

    def mutate_add_step(self, max_force):
        rand = random.randint(0, len(self.route) - 1)
        self.route.insert(rand, self.create_random_step(max_force))

    def mutate_delete_step(self):
        rand = random.randint(0, len(self.route) - 1)
        self.route.pop(rand)

    def create_random_step(self, max_force):
        return Vector2D.create_random_vector() * (random.random() * max_force)

    @classmethod
    def breed(cls, parent1, parent2):
        if len(parent1.route) < len(parent2.route):
            min_parent, max_parent = parent1, parent2
        else:
            min_parent, max_parent = parent2, parent1

        rand = random.randint(0, len(min_parent.route))
        new_individual = Individual()
        for i in range(0, rand):
            new_individual.add_step(min_parent.route[i])
        for i in range(rand, len(max_parent.route)):
            new_individual.add_step(max_parent.route[i])
        return new_individual


