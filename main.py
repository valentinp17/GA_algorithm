import pygame
import sys
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE


COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (195, 195, 195),
}

class Simulation:
    def __init__(self):
        pygame.init()

        self.screen_size = (1000, 1000)
        self.screen = pygame.display.set_mode(self.screen_size, HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.screen.fill(COLORS['white'])
        pygame.display.set_caption('AG Algorithm')

        self.clock = pygame.time.Clock()


        self.init_sim()

    def check_input(self):
        pass #TODO

    def init_sim(self):
        pass #TODO

    def update_sim(self):
        pass #TODO

    def draw_background(self):
        self.screen.fill(COLORS['white'])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    pass #TODO

            self.clock.tick(60)
            self.draw_background()
            self.update_sim()

            pygame.display.flip()


if __name__ == '__main__':
    Simulation().run()