import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 760

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("blue")
    pygame.display.flip()
    clock.tick(60)