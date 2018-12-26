import pygame
import sys
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE

from circle import Circle
from vector2d import Vector2D
from robot import Robot

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (195, 195, 195),
    'red': (255, 0, 0),
}
COEFFICIENT = 8 # 1 pixel = COEFF
MAX_F = 1 / 800


class Simulation:
    def __init__(self):
        pygame.init()

        self.screen_size = (1000, 1000)
        self.screen = pygame.display.set_mode(self.screen_size, HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.screen.fill(COLORS['white'])
        pygame.display.set_caption('AG Algorithm')

        self.clock = pygame.time.Clock()
        self.robot = Robot(100, 100)

        self.init_sim()

    def check_input(self):
        pass #TODO

    def init_sim(self):
        pass #TODO

    def update_sim(self, circles):
        self.robot.move(circles, 0.00000000000000001)

    def draw_objects(self, circles):
        pygame.draw.ellipse(self.screen, COLORS['black'], [self.robot.position.x, self.robot.position.y, 8, 8])
        print(self.robot, self.robot.get_score())

        for circle in circles:
            pygame.draw.ellipse(self.screen, COLORS['red'],
                                [circle.position.x, circle.position.y, circle.radius, circle.radius])

    def draw_background(self):
        self.screen.fill(COLORS['white'])
        pygame.draw.line(self.screen, COLORS['gray'], (100-COEFFICIENT, 100-COEFFICIENT),
                         (100-COEFFICIENT, 900-COEFFICIENT), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (100 - COEFFICIENT, 100 - COEFFICIENT),
                           (900 - COEFFICIENT, 100 - COEFFICIENT), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (900 - COEFFICIENT, 100 - COEFFICIENT),
                         (900 - COEFFICIENT, 900 - COEFFICIENT), 5)
        pygame.draw.line(self.screen, COLORS['gray'], (100 - COEFFICIENT, 900 - COEFFICIENT),
                         (900 - COEFFICIENT, 900 - COEFFICIENT), 5)

    def run(self, circles):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    pass #TODO

            self.clock.tick(60)
            self.update_sim(circles)
            self.draw_background()
            self.draw_objects(circles)



            pygame.display.flip()


if __name__ == '__main__':
    circles = [Circle(500, 500, 100), Circle(700, 700, 100)]
    Simulation().run(circles)

