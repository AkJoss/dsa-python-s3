# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:23:38 2024

@author: José Alberto Rocha Munguía
"""

"""
Regular enemy for Galatsia (falls down; multi-sprite health / explosion).
"""
import pygame
import random


class Enemy:
    def __init__(self, images=None):
        self.x = random.randint(0, 750)
        self.y = random.randint(-100, -40)
        self.width = 50
        self.height = 40
        self.images = images
        self.current_image = 0
        self.color = (219, 97, 255)
        self.velocity = random.randint(1, 5)
        # Health is based on the number of available sprites
        self.health = len(images) - 1 if images else 3
        self.explosion_timer = 30
        
    def move(self):
        """Moves the enemy downward. Resets position if it crosses the bottom boundary."""
        self.y += self.velocity
        if self.y > 600: 
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, 750)
            
    def draw(self, screen):
        """Renders the current enemy sprite or an explosion if dead."""
        if self.health > 0:
            if self.images and self.current_image < len(self.images):
                screen.blit(pygame.transform.scale(self.images[self.current_image], (self.width, self.height)), (self.x, self.y))
            else: 
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.explosion_timer > 0:
            # Show the last image (explosion) for a limited time
            screen.blit(pygame.transform.scale(self.images[-1], (self.width, self.height)), (self.x, self.y))
            self.explosion_timer -= 1
    
    def collides_with(self, obj):
        """Checks for collision using Pygame's Rect objects."""
        if self.health > 0:
            return self.get_rect().colliderect(obj.get_rect())
        return False
    
    def get_rect(self):
        """Returns the enemy's hitbox."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update_sprite(self):
        """Updates the current image based on damage received."""
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
        else:
            self.health = 0
            
    def is_dead(self):
        """Checks if the enemy health is zero and the explosion animation finished."""
        return self.health <= 0 and self.explosion_timer <= 0