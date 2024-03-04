import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, flip, pos):
        super().__init__()
        self.flip = flip
        self.image = pygame.transform.flip(pygame.image.load(image).convert_alpha(), False, flip)
        self.initial_pos = pos[1]
        self.direction = 2
        self.rect = self.image.get_rect(midtop = pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, world_shift, movement):
        self.rect.x -= world_shift
        if movement:
            if self.rect.top >= self.initial_pos + 50:
                self.direction *= -1
            elif self.rect.top <= self.initial_pos - 50:
                self.direction *= -1
            self.rect.top += self.direction
        if self.rect.x < -500:
            self.kill()