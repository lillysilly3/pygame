import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        # generating random angles for smaller asteroids to bounce once created
        random_angle = random.uniform(20, 50)
            
        new_asteroid1_velocity = self.velocity.rotate(random_angle)
        new_asteroid2_velocity = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            
        new_asteroid1 = Asteroid(*self.position, new_asteroid_radius)
        new_asteroid2 = Asteroid(*self.position, new_asteroid_radius)

        new_asteroid1.velocity = new_asteroid1_velocity * 1.2
        new_asteroid2.velocity = new_asteroid2_velocity * 1.2