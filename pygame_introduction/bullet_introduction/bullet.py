import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (screen_width/2,screen_height/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        return Bullet(self.rect.centerx + 50, self.rect.centery)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (x,y))

    def update(self):
        self.rect.x += 5
        if self.rect.left > screen_width:
            self.kill()


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.shoot())
    screen.fill("black")
    bullet_group.update()
    bullet_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(120)