# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:27:02 2024

@author: José Alberto Rocha Munguía
"""

"""
Galatsia — space shooter pygame game (DSA coursework).

Run from this folder so images/ and music/ resolve.

Controls:
  WASD  move
  SPACE shoot
  C     special clear (cooldown bar)

Quick test:
  /opt/anaconda3/bin/python3 main.py
  Expect window "GALATSIA", ambient music, score/lives UI.
"""
import pygame
from player import Player
from bullets import Bullet
from enemy import Enemy
from special_enemy import SpecialEnemy
import random

pygame.init()
pygame.mixer.init(buffer=512)

# Screen configuration
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GALATSIA")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
GRAY = (169, 169, 169)

# Music and sounds loading
pygame.mixer.music.load("music/ambience_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

sound_shot = pygame.mixer.Sound("music/sound_shot.mp3")
sound_shot.set_volume(0.15)

sound_enemy_dead = pygame.mixer.Sound("music/enemy_dead.mp3")
sound_enemy_dead.set_volume(0.5)

sound_auch = pygame.mixer.Sound("music/auch.mp3")
sound_auch.set_volume(0.5)

sound_super_dead = pygame.mixer.Sound("music/super_dead.mp3")
sound_super_dead.set_volume(0.5)

# Dedicated sound channels
enemy_dead_channel = pygame.mixer.Channel(0)
auch_channel = pygame.mixer.Channel(1)

# Images loading
bullet_image = pygame.image.load("images/fire_bullet.png")
enemy_images = [
                pygame.image.load("images/enemy_1.png"),
                pygame.image.load("images/enemy_2.png"),
                pygame.image.load("images/enemy_3.png"),
                pygame.image.load("images/explotion.png"),
]
special_enemy_image = pygame.image.load("images/ovni.png")
special_enemy_explosion = pygame.image.load("images/explotion_2.png")
player_image = pygame.image.load("images/halcon.png")

# Initializing the player and game lists
player = Player(WIDTH//2, HEIGHT-50, player_image)
bullets = []
enemies = []
special_enemies = []
score = 0
level = 1
special_power_ready = True
special_power_cooldown = 10000 
last_special_use = 0

# Special enemy spawn config
special_enemy_spawn_chance = 0.0010
enemy_spawn_counter = 0
enemy_speed_increase = 0

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# Main game loop
running = True
game_over = False

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + player.width // 2, player.y, bullet_image))
                sound_shot.play()
            elif event.key == pygame.K_c and special_power_ready and not game_over:
                enemies.clear()
                special_enemies.clear()
                special_power_ready = False
                last_special_use = pygame.time.get_ticks()
                
    if game_over: 
        pygame.mixer.music.stop()
        sound_super_dead.play()
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width()//2, HEIGHT // 2-50))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width()//2, HEIGHT // 2 + 20))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
        continue
        
    # Special Power Cooldown Logic
    current_time = pygame.time.get_ticks()
    if not special_power_ready:
        elapsed_time = current_time - last_special_use
        if elapsed_time >= special_power_cooldown:
            special_power_ready = True
        else:
            bar_width = int((elapsed_time / special_power_cooldown) * 200)
            pygame.draw.rect(screen, GRAY, (10, 130, 200, 20))
            pygame.draw.rect(screen, BLUE, (10, 130, bar_width, 20))
    else:
        pygame.draw.rect(screen, BLUE, (10, 130, 200, 20))
        
    # Level and Difficulty Scaling
    if score >= level * 100:
        level += 1
        enemy_speed_increase += 1
        enemy_spawn_counter = max(20, enemy_spawn_counter - 10)
        
    # Enemy Spawning
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= 60:
        new_enemy = Enemy(images=enemy_images)
        new_enemy.velocity += enemy_speed_increase
        enemies.append(new_enemy)
        enemy_spawn_counter = 0
        
    # Special Enemy Spawning
    if random.random() < special_enemy_spawn_chance:
        special_enemy = SpecialEnemy(image=special_enemy_image, explosion_image=special_enemy_explosion)
        special_enemy.velocity += enemy_speed_increase
        special_enemies.append(special_enemy)
    
    # Player update
    player.move()
    player.draw(screen)
    
    # HUD Display
    lives_text = font.render(f"Lives: {player.lives}", True, (255 ,255 ,255))
    screen.blit(lives_text, (10, 10))
    score_text = font.render(f"Score: {score}", True, (255 ,255 ,255))
    screen.blit(score_text, (10, 50))
    level_text = font.render(f"Level: {level}", True, (255 ,255 ,255))
    screen.blit(level_text, (10, 90))
    
    # Bullets update
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        if bullet.y < 0:
            bullets.remove(bullet)

    # Enemies update and collision check
    for enemy in enemies[:]:
        enemy.move()
        enemy.draw(screen)
        for bullet in bullets[:]:
            if enemy.collides_with(bullet):
                bullets.remove(bullet)
                enemy.update_sprite()
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)
                    score += 10
                    enemy_dead_channel.play(sound_enemy_dead)
        
        if enemy.collides_with(player):
            player.lives -= 1
            auch_channel.play(sound_auch)
            enemies.remove(enemy)
            if player.lives <= 0:
                game_over = True
                
        if enemy.is_dead():
            enemies.remove(enemy)
            
    # Special Enemies update
    for special_enemy in special_enemies[:]:
        special_enemy.move()
        special_enemy.draw(screen)
        for bullet in bullets[:]:
            if special_enemy.collides_with(bullet):
                bullets.remove(bullet)
                special_enemy.health -= 1
                if special_enemy.health <= 0 :
                    special_enemies.remove(special_enemy)
                    score += 50
                    enemy_dead_channel.play(sound_enemy_dead)
                    
        if special_enemy.collides_with(player):
            player.lives -= 1
            auch_channel.play(sound_auch)
            special_enemies.remove(special_enemy)
            if player.lives <= 0:
                game_over = True
        
        if special_enemy.is_dead():
            special_enemies.remove(special_enemy)
                
    pygame.display.flip()
    pygame.time.delay(30)
    
pygame.quit()