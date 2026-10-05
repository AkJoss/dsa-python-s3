"""
Special Enemy (DSA coursework).

@author José Alberto Rocha Munguía
"""

import pygame
import random

class SpecialEnemy:
    def __init__(self, image=None, explosion_image=None):
        self.x = random.randint(0, 750)
        self.y = random.randint(-100, -40)
        self.width = 65
        self.height = 50
        self.image = image
        self.explosion_image = explosion_image
        self.color = (125, 15, 157)
        self.velocity = random.randint(3, 5)
        self.health = 5
        self.explosion_timer = 30
        
    def move(self):
        self.y += self.velocity
        if self.y > 600:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, 750)
            
    def draw(self, screen):
        if self.health > 0:
            if self.image:
                screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
            else:
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.explosion_timer > 0:
            if self.explosion_image:
                screen.blit(pygame.transform.scale(self.explosion_image, (self.width, self.height)), (self.x, self.y))
            self.explosion_timer -= 1
            
    def collides_with(self, obj):
        if self.health > 0:
            return self.get_rect().colliderect(obj.get_rect())
        return False
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
            
    def is_dead(self):
        return self.health <= 0 and self.explosion_timer <= 0