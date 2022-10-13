from os import system
import pygame

# This section will contain blider,music.

# Initialize pygame
pygame.init()


# Defile colors as RGB tuples
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGNETA = (255,0,255)

# display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
WINDOW = (WINDOW_WIDTH,WINDOW_HEIGHT)
caption = "Vincent practice 2"
display_surface = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(caption)

# display background
display_surface.fill(WHITE)

# define fonts
system_font = pygame.font.SysFont('calibri',40)
custom_font_src = '../Tutorials/font/2D_classic.ttf'
custom_font = pygame.font.Font(custom_font_src,32)

# define text
system_text = system_font.render("Cat Rule",True,GREEN,WHITE)
system_text_rect = system_text.get_rect()
system_text_rect.topleft = (WINDOW_WIDTH//2 - 60 ,10)

custom_text = custom_font.render("Move the catty soon!",True,RED,WHITE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2,100)

# create images
cat_left_img_src = "../Tutorials/Icon/Cat-icon-left.png"
cat_left_img = pygame.image.load(cat_left_img_src)
cat_left_rect = cat_left_img.get_rect()
cat_left_rect.topleft = (0,0)

cat_right_img_src = "../Tutorials/Icon/Cat-icon-right.png"
cat_right_img = pygame.image.load(cat_right_img_src)
cat_right_rect = cat_right_img.get_rect()
cat_right_rect.topright = (WINDOW_WIDTH,0)

pygame.draw.line(display_surface,RED,(0,75),(WINDOW_WIDTH,75),4)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    # Copy a surface object at the given coordinates to our display(image)
    display_surface.blit(cat_left_img,cat_left_rect)
    display_surface.blit(cat_right_img,cat_right_rect)
    
    # Copy a surface object at the given coordinates to our display(text)
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    
    # Update the display
    pygame.display.update()

pygame.quit()
