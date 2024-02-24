import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((40,40))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (300,300))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img.png")
        self.rect = self.image.get_rect(center = (400,400))
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

player = pygame.sprite.GroupSingle(Player())
obstacle = pygame.sprite.GroupSingle(Obstacle())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")
    player.update()
    player.draw(screen)
    obstacle.draw(screen)

    if pygame.sprite.spritecollide(player.sprite, obstacle,False):
        if pygame.sprite.spritecollide(player.sprite, obstacle,False, pygame.sprite.collide_mask):
            player.sprite.image.fill("green")
        else:
            player.sprite.image.fill("red")

    pygame.display.flip()
    clock.tick(60)