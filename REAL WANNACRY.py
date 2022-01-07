import pygame, sys
from pygame.locals import *
from wanna_resources import background_string, icon_string
import base64


# set up pygame
pygame.init()

with open('wanna.WCRY', 'wb') as imagef:
    imagef.write(base64.b64decode(background_string))

with open('icon.WCRY', 'wb') as imagef:
    imagef.write(base64.b64decode(icon_string))

# set up the window
windowSurface = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN, 32)
a = pygame.image.load('icon.WCRY')
pygame.display.set_icon(a)
pygame.display.set_caption('Do you WannaCry yet?')
# q = pygame.image.load('WannaCry.jpg').convert()
q = pygame.image.load('wanna.WCRY').convert()
x = 20; # x coordnate of image
y = 30; # y coordinate of image
windowSurface.blit(q, ( x,y)) # paint to screen
pygame.display.flip() # paint screen one time

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# run the game loop

while True:
    windowSurface.fill(BLACK)
    windowSurface.blit(q, ( x,y)) # paint to screen
    # pygame.display.flip() # paint screen one time

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()