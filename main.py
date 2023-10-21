import pygame
import sys
from settings import Settings
from ufo import Ufo
from pipe import Pipe

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Adventure 2023")
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("2205_w026_n002_1983b_p1_1983.jpg")
        self.background = pygame.transform.scale(self.background, (self.settings.screen_width, self.settings.screen_height))
        self.background_x = 0

        self.pipe = Pipe(self.settings.screen_width, self.settings.screen_height, 50, 200)

        self.ufo = Ufo(self)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ufo.move_up = True
                    if event.key == pygame.K_q:
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.ufo.move_up = False

            self.background_x -= 2

            if self.background_x <= -self.settings.screen_width:
                self.background_x = 0

            self.screen.blit(self.background, (self.background_x, 0))
            self.screen.blit(self.background, (self.background_x + self.settings.screen_width, 0))

            self.ufo.blit_me()
            self.ufo.update()

            self.pipe.move()
            self.pipe.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    game = Game()
    game.run()

