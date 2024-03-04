import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, create_jump_particles):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.2
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.2
        self.display_surface = screen
        self.create_jump_particles = create_jump_particles

        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_character_assets(self):
        character_path = "graphics/character/"
        self.animations = {"idle": [], "run": [],"jump": [], "fall": []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder("graphics/character/dust_particles/run")

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

        #set rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)

    def dust_animation(self):
        if self.status == "run" and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0
            dust_particles = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particles, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                dust_particles = pygame.transform.flip(dust_particles, True, False)
                self.display_surface.blit(dust_particles, pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x += 1
            self.facing_right = True
        if keys[pygame.K_LEFT]:
            self.direction.x += -1
            self.facing_right = False
        if keys[pygame.K_UP]:
            if self.on_ground:
                self.jump()
                self.create_jump_particles(self.rect.midbottom)

    def get_state(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 0:
            self.status = "fall"
        elif self.direction.x != 0:
            self.status = "run"
        elif self.direction.x == 0:
            self.status = "idle"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_state()
        self.animate()
        self.dust_animation()