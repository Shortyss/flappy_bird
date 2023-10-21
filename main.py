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

        self.score = 0

        pygame.display.set_caption("Space Adventure 2023")
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("2205_w026_n002_1983b_p1_1983.jpg")
        self.background = pygame.transform.scale(self.background, (self.settings.screen_width, self.settings.screen_height))
        self.background_x = 0

        self.pipe = Pipe(self.settings.screen_width, self.settings.screen_height, 50, 200)

        self.ufo = Ufo(self)

    def display_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Score" + str(self.score), True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 10))
        self.screen.blit(text, text_rect)

    def game_over(self):
        font = pygame.font.Font(None, 46)
        text = font.render(f"GAME OVER! \n For restart type R or Q for quit.", True, (255,0, 0))
        text_rect = text.get_rect(center=(self.settings.screen_width / 2, self.settings.screen_height / 2))
        self.screen.blit(text,text_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def restart_game(self):
        self.pipe = Pipe(self.settings.screen_width, self.settings.screen_height, 50, 200)
        self.ufo = Ufo(self)
        self.score = 0
        self.run()

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

            if self.pipe.pipe_x < self.ufo.rect.right:
                if not (self.ufo.rect.bottom < self.pipe.top_pipe_height and
                        self.ufo.rect.top > self.pipe.top_pipe_height - self.pipe.gap_height):
                    self.game_over()
                else:
                    if self.pipe.pipe_x < self.ufo.rect.left:
                        self.score += 1

            if self.ufo.rect.bottom >= self.settings.screen_height:
                self.game_over()

            self.display_score()

            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    game = Game()
    game.run()

