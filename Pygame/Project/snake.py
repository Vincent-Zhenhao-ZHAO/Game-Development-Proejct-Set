from cProfile import run
from pickle import FALSE
from turtle import window_height
from pygame import mixer
import pygame;
import random

from sqlalchemy import false;

pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW = (WINDOW_WIDTH,WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(WINDOW)
pygame.display.set_caption("~~Snake Game~~")

# Set FPS
fps = 20
clock = pygame.time.Clock()


# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
RED = (250,0,0)
DARKRED = (150,0,0)
WHITE = (255,255,255)

# Set fonts
font = pygame.font.SysFont('gabriola',48)

# Set text
title_text = font.render("~~I~am~a~snake~~",True,GREEN,DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

score_text = font.render("~~Score~~" + str(score),True,GREEN,DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

game_over_text = font.render("~~~~YOU~EAT~YOURSELF~~~~",True,RED,DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text = font.render("~~Press~~any~~key~~Be~~again~~snake~~~",True,RED,DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2 + 64)

# Set music and sounds

pick_up_sound = pygame.mixer.Sound("./PickUp.wav")

mixer.init()
mixer.music.load('./background.wav')
mixer.music.play(loops=-1)

# Set images
apple_pos = (500,500,SNAKE_SIZE,SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface,RED,apple_pos)

head_pos = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface,RED,head_pos)

body_pos = []

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = SNAKE_SIZE
                snake_dx = 0
            elif event.key == pygame.K_UP:
                snake_dy = -SNAKE_SIZE
                snake_dx = 0
    
    body_pos.insert(0, head_pos)
    body_pos.pop()            
    
    # Update the snake
    head_x += snake_dx
    head_y += snake_dy
    
    head_pos = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
    
    # Check game over
    if head_pos in body_pos:
        display_surface.blit(game_over_text,game_over_rect)
        display_surface.blit(continue_text,continue_rect)
        pygame.display.update()
        
        # pause
        is_pasue = True
        while is_pasue:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    score = 0
                    head_x = WINDOW_WIDTH // 2
                    head_y = WINDOW_HEIGHT // 2 + 50
                    head_pos = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
                    body_pos = []
                    snake_dx = 0
                    snake_dy = 0
                    is_pasue = False
                    
                elif event.type == pygame.QUIT:
                    is_pasue = False
                    running = False
    
    # Check collision
    
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_pos = (apple_x,apple_y,SNAKE_SIZE,SNAKE_SIZE)
        
        body_pos.append(head_pos)
    
    # Update score
    score_text = font.render("~~Score~~" + str(score),True,GREEN,DARKRED)
    
    # Fill surface
    display_surface.fill(WHITE)
    
    # Blit HUD
    display_surface.blit(title_text,title_rect)
    display_surface.blit(score_text,score_rect)
    
    # Blit assets
    
    for body in body_pos:
        pygame.draw.rect(display_surface,RED,body)
    
    
    head_rect = pygame.draw.rect(display_surface,GREEN,head_pos)
    apple_rect = pygame.draw.rect(display_surface,RED,apple_pos)
    
    
    
    pygame.display.update()
    clock.tick(fps)
    
    
pygame.quit()