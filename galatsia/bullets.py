# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:55:52 2024

@author: José Alberto Rocha Munguía
"""

"""
Player bullet for Galatsia (moves upward; sprite or circle fallback).
"""
import pygame


class Bullet:
    def __init__(self, x, y, image=None):
       self.x = x
       self.y = y
       self.radius = 5
       self.width = 10
       self.height = 20
       self.color = (239, 83, 80) # Pastel red color
       self.velocity = -10 # Moves upward
       self.image = image
       
    def move(self):
        """Moves the bullet upward across the screen."""
        self.y += self.velocity
          
    def draw(self, screen):
        """Renders the bullet image or a circle if no image is loaded."""
        if self.image:
            screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            
    def get_rect(self):
        """Returns the bullet's rect for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.height)