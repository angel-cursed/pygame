import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_1.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_2.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_3.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_4.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_5.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_6.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_7.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_8.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_9.png"), (400,200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("attack_10.png"), (400,200)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

moving_sprites = pygame.sprite.Group()
player = Player(10,10)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
    moving_sprites.update(0.25)
    screen.fill("black")
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)