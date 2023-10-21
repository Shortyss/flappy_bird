import pygame
import sys
from settings import Settings


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode(0, 0)

        self.settings.screen_width = self.settings.screen_width
        self.settings.screen_height = self.settings.screen_height


    def run(self):
        while True:
            pass


if __name__ == "__main__":
    game = Game()
    game.run()
