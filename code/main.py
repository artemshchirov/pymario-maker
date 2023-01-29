import pygame
import time
from settings import *
from pygame.image import load
from support import get_path
from editor import Editor


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.editor = Editor()

        # cursor
        surf = load(get_path('../graphics/cursors/mouse.png')).convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), surf)
        pygame.mouse.set_cursor(cursor)

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
