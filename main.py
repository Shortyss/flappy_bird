import pygame
import sys
from settings import Settings


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Adventure 2023")
        self.clock = pygame.time.Clock()

        self.backgroud = pygame.image.load("2205_w026_n002_1983b_p1_1983.jpg")
        self.backgroud = pygame.transform.scale(self.backgroud, (self.settings.screen_width, self.settings.screen_height))
        self.backgroud_x = 0


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.backgroud_x -= 2

            if self.backgroud_x <= -self.settings.screen_width:
                self.backgroud_x = 0

            self.screen.blit(self.backgroud, (self.backgroud_x, 0))
            self.screen.blit(self.backgroud, (self.backgroud_x + self.settings.screen_width, 0))

            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    game = Game()
    game.run()

