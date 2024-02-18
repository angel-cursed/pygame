import random

import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("shoot.mp3")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, x, y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")
background = pygame.image.load("BG.png")
background = pygame.transform.scale(background, screen.get_size())
pygame.mouse.set_visible(False)


crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for i in range(20):
    target = Target("target.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    if not target_group:
        for i in range(20):
            target = Target("target.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
            target_group.add(target)

    crosshair_group.update()
    screen.blit(background, (0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
