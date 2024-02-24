import pygame, sys

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = pickaxe.get_rect(center = (screen_width/2, screen_height/2))

    return rotated_surface, rotated_rect

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

pickaxe = pygame.image.load("pickaxe.png")
pickaxe_rect = pickaxe.get_rect(center = (screen_width/2, screen_height/2))
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle += 1
    screen.fill("white")
    pickaxe_rotated, pickaxe_rotated_rect = rotate(pickaxe, angle)
    screen.blit(pickaxe_rotated, pickaxe_rotated_rect)
    pygame.display.flip()
    clock.tick(60)