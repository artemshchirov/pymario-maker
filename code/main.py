import pygame
import time
from settings import *
from editor import Editor


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.editor = Editor()

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()

            self.editor.run(dt)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    main = Main()
    main.run()
