import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand = random.uniform(20, 50)
            vect1 = self.velocity.rotate(-rand)
            vect2 = self.velocity.rotate(rand)
            splitRad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, splitRad)
            ast1.velocity = vect1 * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, splitRad)
            ast2.velocity = vect2 * 1.2
        self.kill()
