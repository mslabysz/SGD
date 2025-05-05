import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

WIDTH, HEIGHT = 400, 300
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Cats Animation')

WHITE = (255, 255, 255)

catImg = pygame.image.load('cat.png')
cat_width, cat_height = catImg.get_width(), catImg.get_height()

cat1_x = 10
cat1_y = 10
cat1_dx = 5
cat1_dy = 0

cat2_x = 200
cat2_y = 150
cat2_dx = 3
cat2_dy = 4

while True:
    DISPLAYSURF.fill(WHITE)

    if cat1_dx > 0:  # right
        cat1_x += cat1_dx
        if cat1_x >= WIDTH - cat_width - 10:
            cat1_dx = 0
            cat1_dy = 5
    elif cat1_dy > 0:  # down
        cat1_y += cat1_dy
        if cat1_y >= HEIGHT - cat_height - 10:
            cat1_dy = 0
            cat1_dx = -5
    elif cat1_dx < 0:  # left
        cat1_x += cat1_dx
        if cat1_x <= 10:
            cat1_dx = 0
            cat1_dy = -5
    elif cat1_dy < 0:  # up
        cat1_y += cat1_dy
        if cat1_y <= 10:
            cat1_dy = 0
            cat1_dx = 5

    cat2_x += cat2_dx
    cat2_y += cat2_dy

    if cat2_x <= 0 or cat2_x >= WIDTH - cat_width:
        cat2_dx *= -1
    if cat2_y <= 0 or cat2_y >= HEIGHT - cat_height:
        cat2_dy *= -1

    DISPLAYSURF.blit(catImg, (cat1_x, cat1_y))
    DISPLAYSURF.blit(catImg, (cat2_x, cat2_y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)