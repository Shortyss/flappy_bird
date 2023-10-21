import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_screen = pygame.image.load("2205_w026_n002_1983b_p1_1983.jpg")
        self.fps = 60
