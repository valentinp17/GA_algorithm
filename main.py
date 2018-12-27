import pygame
import sys
import random
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE, SRCALPHA
from pygame import gfxdraw


from circle import Circle
from vector2d import Vector2D
from robot import Robot

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (195, 195, 195),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
}
COEFFICIENT = 8 # 1 pixel = COEFF
MAX_F = 5


class Simulation:
    def __init__(self, primary_vectors):
        pygame.init()

        self.screen_size = (1000, 1000)
        self.screen = pygame.display.set_mode(self.screen_size, HWSURFACE|DOUBLEBUF|RESIZABLE|SRCALPHA)
        self.screen.fill(COLORS['white'])
        pygame.display.set_caption('AG Algorithm')
        self.font = pygame.font.Font(None, 30)
        self.is_pause = False
        self.current_generation = 0

        self.clock = pygame.time.Clock()
        self.population = create_initial_population(500, primary_vectors)

        self.init_sim()

    def check_input(self, event):
        if event.key == pygame.K_SPACE:
            if self.is_pause:
                self.is_pause = False
            else:
                self.is_pause = True


    def init_sim(self):
        pass

    def update_sim(self, circles):
        counter_alive_robots = 0
        for robot in self.population:

            if robot.is_alive:
                #print(robot, robot.current_step)
                robot.make_step(circles)
                counter_alive_robots += 1
            else:
                pass


        if counter_alive_robots == 0:
            self.population = next_generation(self.population, 50, 0.5)

            self.current_generation += 1
            #print(self.current_generation)



    def draw_objects(self, circles):
        for circle in circles:
            pygame.gfxdraw.filled_circle(self.screen, int(circle.position.x), int(circle.position.y),
                                         circle.radius, (255, 0, 0, 255))

        for robot in self.population:
            if robot.is_alive:
                robot_color = (0, 255, 0, 100)
            else:
                robot_color = (100, 100, 100, 100)
            pygame.gfxdraw.filled_circle(self.screen, int(robot.position.x), int(robot.position.y),
                                         8, robot_color)
        self.draw_grid()

    def draw_info(self):
        text = self.font.render(f'Generation:{self.current_generation}', 1, (0, 0, 0))
        self.screen.blit(text, (10, 10))


    def draw_background(self):
        self.screen.fill(COLORS['white'])

    def draw_grid(self):
        pygame.draw.line(self.screen, COLORS['gray'], (100, 100),
                         (100, 900), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (100, 100),
                         (900, 100), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (900, 100),
                         (900, 900), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (100, 900),
                         (900, 900), 5)

    def run(self, circles):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_input(event)
                elif event.type == pygame.VIDEORESIZE:
                    pass

            self.clock.tick()

            if not self.is_pause:
                #pygame.time.delay(100)
                self.update_sim(circles)
                self.draw_background()
                self.draw_objects(circles)
                self.draw_info()

            pygame.display.flip()


def create_route(vectors):
    route = random.sample(vectors[:], len(vectors))
    return route


def create_initial_population(population_size, vectors):
    population = []
    for i in range(population_size):
        r = Robot(100, 100)
        r.add_route(create_route(vectors))
        population.append(r)
    return population


def get_ranked_robots(population):
    return sorted(population, key=lambda x: x.fitness, reverse=True)[:]


def selection(population_ranked, elite_size):
    """
        Наверно надо что-то получше здесь придумать
    """
    selection_results = population_ranked[:elite_size]
    return selection_results[:]


def mutate(robot, mutation_rate):
    for i in range(len(robot.route)):
        if random.random() < mutation_rate:
            changing_vector = random.randint(0, len(robot.route) - 1)
            robot.route[changing_vector] = robot.route[changing_vector] * \
                                          Vector2D(random.random(), random.random())
    return robot.__copy__()


def mutate_population(population, mutation_rate):
    return [mutate(robot.__copy__(), mutation_rate) for robot in population]


def next_generation(current_generation, elite_size, mutation_rate):
    pop_ranked = get_ranked_robots(current_generation)
    selection_results = selection(pop_ranked, elite_size)
    next_generation = []
    for i in range(0, 5):
        next_generation.extend(mutate_population(selection_results[:], mutation_rate)[:])
    for robot in next_generation:
        robot.reset(100, 100)
    return next_generation


def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = create_initial_population(pop_size, primary_vectors)
    for i in range(generations):
        pop = next_generation(pop, elite_size, mutation_rate)

    best_robot = get_ranked_robots(pop)[0]
    return  best_robot

def create_random_vector():
    x = random.random()
    return Vector2D(x, 1 - x)

def get_random_force(max_force):
    return random.random() * max_force

if __name__ == '__main__':
    circles = [Circle(100, 900, 300), Circle(700, 500, 300)]
    primary_vectors = [create_random_vector() * get_random_force(MAX_F) for x in range(100)]
    #best_robot = genetic_algorithm(primary_vectors, 100, 50, 0.1, 1000)
    #print(best_robot, best_robot.fitness)
    Simulation(primary_vectors).run(circles)

