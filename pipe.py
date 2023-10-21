import pygame
import random

class Pipe:
    def __init__(self, screen_width, screen_height, pipe_width, gap_height):
        self.pipe_x = screen_width
        self.pipe_width = pipe_width
        self.pipe_speed = 5
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pipe_color = (102, 102, 0)
        self.gap_height = gap_height

        self.generate_pipe()

    def generate_pipe(self):
        # Náhodné umístění horní a dolní trubky
        self.top_pipe_height = random.randint(50, self.screen_height - self.gap_height - 50)
        self.bottom_pipe_height = self.screen_height - self.gap_height - self.top_pipe_height

    def move(self):
        self.pipe_x -= self.pipe_speed
        if self.pipe_x < -self.pipe_width:
            self.pipe_x = self.screen_width
            self.generate_pipe()

    def draw(self, screen):
        pygame.draw.rect(screen, self.pipe_color, (self.pipe_x, 0, self.pipe_width, self.top_pipe_height))
        pygame.draw.rect(screen, self.pipe_color, (self.pipe_x, self.screen_height - self.bottom_pipe_height, self.pipe_width, self.bottom_pipe_height))
