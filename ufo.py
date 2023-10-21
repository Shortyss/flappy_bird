import pygame


class Ufo():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("UFO1.png")

        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.move_up = False

        gravity = 1
        velocity = 0

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

