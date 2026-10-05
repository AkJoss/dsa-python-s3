# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:37:59 2024

@author: José Alberto Rocha Munguía
"""
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
MARGIN = 10
ROWS = 4
COLS = 4
CARD_SIZE = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CRAZY_RED = (223, 68, 68)
DARK_BLUE = (30, 77, 148)

# Load images (Ensure these files are in the same folder)
image_files = [
    "watermelon.png", "banana.png", "guava.png", "tomato.png",
    "apple.png", "grape.png", "orange.png", "pear.png"
]

# Note: Using placeholders if images are missing; replace with your local paths
try:
    card_images = [pygame.image.load(img) for img in image_files]
    back_image = pygame.image.load("brain.png")
except:
    # Fallback if images aren't found during translation test
    card_images = [pygame.Surface((CARD_SIZE, CARD_SIZE)) for _ in image_files]
    back_image = pygame.Surface((CARD_SIZE, CARD_SIZE))

# Scale images
card_images = [pygame.transform.scale(img, (CARD_SIZE, CARD_SIZE)) for img in card_images]
back_image = pygame.transform.scale(back_image, (CARD_SIZE, CARD_SIZE))

class Stack:
    """Stack data structure for game moves."""
    def __init__(self):
        self.elements = []
    
    def push(self, item):
        self.elements.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return None
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def clear(self):
        self.elements = []

class Card:
    def __init__(self, card_id, front_image, pos):
        self.card_id = card_id
        self.front_image = front_image
        self.back_image = back_image
        self.is_flipped = False
        self.is_matched = False
        self.pos = pos
        
    def flip(self):
        if not self.is_matched:
            self.is_flipped = not self.is_flipped
        
    def is_match(self, other_card):
        return self.card_id == other_card.card_id
    
    def draw(self, surface):
        if self.is_flipped or self.is_matched:
            surface.blit(self.front_image, self.pos)
        else:
            surface.blit(self.back_image, self.pos)
        pygame.draw.rect(surface, BLACK, (*self.pos, CARD_SIZE, CARD_SIZE), 2)

class MemoryGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Memory Game - Data Structures")
        
        self.selected_cards = []
        self.move_stack = Stack()
        self.cards = []
        self.message = ""
        self.timer = 0
        self.game_over = False
        
        # Buttons
        button_width, button_height = 120, 30
        self.restart_btn = pygame.Rect(WINDOW_WIDTH // 2 - 140, WINDOW_HEIGHT - 60, button_width, button_height)
        self.exit_btn = pygame.Rect(WINDOW_WIDTH // 2 + 20, WINDOW_HEIGHT - 60, button_width, button_height)
        
        self.create_board()
        
    def create_board(self):
        self.cards = []
        card_ids = list(range(len(card_images))) * 2
        random.shuffle(card_ids)
        
        h_space = (WINDOW_WIDTH - (COLS * CARD_SIZE) - ((COLS - 1) * MARGIN)) // 2
        v_space = (WINDOW_HEIGHT - 100 - (ROWS * CARD_SIZE) - ((ROWS - 1) * MARGIN)) // 2
        
        for r in range(ROWS):
            for c in range(COLS):
                cid = card_ids.pop()
                img = card_images[cid]
                px = h_space + c * (CARD_SIZE + MARGIN)
                py = v_space + r * (CARD_SIZE + MARGIN)
                self.cards.append(Card(cid, img, (px, py)))
                
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                
                if self.restart_btn.collidepoint(mx, my):
                    self.restart_game()
                if self.exit_btn.collidepoint(mx, my):
                    return False
                
                if len(self.selected_cards) < 2:
                    for card in self.cards:
                        if pygame.Rect(*card.pos, CARD_SIZE, CARD_SIZE).collidepoint(mx, my):
                            if not card.is_flipped and not card.is_matched:
                                card.flip()
                                self.selected_cards.append(card)
        return True
    
    def update(self):
        if len(self.selected_cards) == 2:
            c1, c2 = self.selected_cards
            if c1.is_match(c2):
                self.message = "Match!"
                c1.is_matched = True
                c2.is_matched = True
                self.selected_cards = []
            else:
                self.timer += 1
                if self.timer > 40: # Delay to see cards
                    c1.flip()
                    c2.flip()
                    self.selected_cards = []
                    self.timer = 0
                    self.message = ""
        
        if all(c.is_matched for c in self.cards):
            self.game_over = True
            self.message = "You Won! :D"
            
    def draw(self):
        self.screen.fill(WHITE)
        for card in self.cards:
            card.draw(self.screen)
            
        font = pygame.font.SysFont(None, 36)
        
        # Draw Buttons
        pygame.draw.rect(self.screen, CRAZY_RED, self.restart_btn)
        pygame.draw.rect(self.screen, DARK_BLUE, self.exit_btn)
        
        res_txt = font.render("Restart", True, WHITE)
        exit_txt = font.render("Exit", True, WHITE)
        
        self.screen.blit(res_txt, res_txt.get_rect(center=self.restart_btn.center))
        self.screen.blit(exit_txt, exit_txt.get_rect(center=self.exit_btn.center))
        
        msg_txt = font.render(self.message, True, BLACK)
        self.screen.blit(msg_txt, (WINDOW_WIDTH // 2 - 50, 20))
        
        pygame.display.flip()
        
    def restart_game(self):
        self.message = ""
        self.game_over = False
        self.create_board()

def main():

    game = MemoryGame()

    clock = pygame.time.Clock()

    running = True

    while running:

        running = game.handle_events()

        game.update()

        game.draw()

        clock.tick(60)

    pygame.quit()

    sys.exit()


if __name__ == "__main__":

    main()

