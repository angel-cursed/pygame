import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.gravity = 0.5
        self.direction = 0

        self.jump_speed = -8

    def apply_gravity(self):
        self.direction += self.gravity


    def check_jump(self, sound):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.direction = self.jump_speed
            sound.stop()
            sound.play(loops = 0)

    def update(self, events, sound):
        self.apply_gravity()
        self.check_jump(sound)
        self.rect.y += self.direction

