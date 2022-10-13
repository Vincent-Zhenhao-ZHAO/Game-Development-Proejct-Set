# display the surface
import pygame;

# This file contains: Initialization and Display Surface

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
SET_WINDOW = (WINDOW_WIDTH,WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(SET_WINDOW)
title = "Vincent practice 1"
pygame.display.set_caption(title)

# Defile colors as RGB tuples
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGNETA = (255,0,255)

# Give a background color to the display
# display_surface.fill()

# Draw various shapes on our display
# line(surface,color,starting point, 
# ending point, thickness)
# pygame.draw.line(display_surface,BLUE,(0,0),(200,200),5)

# Circle()surface,color,centre,radius,thickness...
# 0 for fill)
# pygame.draw.circle(display_surface, CYAN, (100,100), 4, width=3)

# Rectangle(Surface,color,(top-left x, top-left y, width, height))
# pygame.draw.rect(display_surface, MAGNETA, (300,200,300,100), width=10)


# The main game loop
running = True
while running:
    # loop throuhg a list of event ovject
    for event in pygame.event.get():
        # Quit the game when click the close button
        if event.type == pygame.QUIT:
            running = False
            
    # Update the display
    pygame.display.update()
        
# End the game
pygame.quit()