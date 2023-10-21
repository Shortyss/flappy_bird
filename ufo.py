import pygame


class Ufo():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("UFO1.png")

        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.move_up = False


        self.ufo_velocity = 0
        self.gravity = 1

    def update(self):
        self.ufo_velocity += self.gravity
        if self.move_up:
            self.ufo_velocity = -10

        self.rect.y += self.ufo_velocity

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

