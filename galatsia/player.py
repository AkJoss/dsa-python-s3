# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:34 2024

@author: José Alberto Rocha Munguía
"""

"""
Player ship for Galatsia (WASD movement, lives, sprite).
"""
import pygame


class Player:
    def __init__(self, x, y, image=None):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.color = (61, 114, 147) # Blue color for the ship
        self.velocity = 10
        self.lives = 3
        self.image = image
    
    def move(self):
        """Handles player movement using WASD keys."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x - self.velocity > 0:
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x + self.velocity < 800 - self.width:
            self.x += self.velocity
        if keys[pygame.K_w] and self.y - self.velocity > 0:
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y + self.velocity < 600 - self.height:
            self.y += self.velocity
    
    def draw(self, screen):
        """Draws the player image or a placeholder rectangle."""
        if self.image:
            screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            
    def get_rect(self):
        """Returns the player's hit box for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.height)