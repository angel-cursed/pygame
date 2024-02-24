import pygame, sys

def bouncing_rect():
    global moving_rect, x_speed, y_speed, other_rect, other_speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    if moving_rect.right >= screen_width or moving_rect.left < 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top < 0:
        y_speed *= -1

    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) == 10:
            y_speed *= -1
        if abs(other_rect.top - moving_rect.bottom) == 10:
            y_speed *= -1
        if abs(other_rect.top - moving_rect.bottom) == 10:
            y_speed *= -1
        if abs(other_rect.top - moving_rect.bottom) == 10:
            y_speed *= -1

    pygame.draw.rect(screen, (255,255,255), moving_rect)
    pygame.draw.rect(screen, (255,0,0), other_rect)

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

moving_rect = pygame.Rect((350,350),(100,100))
x_speed, y_speed = 5,4

other_rect = pygame.Rect((300,600),(200,100))
other_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30,30,30))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)