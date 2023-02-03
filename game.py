import sys
import random

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0,0), flags=FULLSCREEN)
s_width, s_height = screen.get_size()

clock = pygame.time.Clock()
FPS = 60

class Game:
    def __init__(self):
        self.run_game()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(FPS)

    def main():
        game = Game()
    if __name__ == '__main__':
        main()