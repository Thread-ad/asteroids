import pygame

from constants import *
from circleshape import *

class Shots(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOTS_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt