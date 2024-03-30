from settings import *
import math

class StackedSprite(pygame.sprite.Sprite):
    def __init__(self, app, name, pos, rot=0):
        self.app = app
        self.name = name
        self.pos = vec2(pos) * TILE_SIZE
        self.player = app.player
        self.group = app.main_group
        super().__init__(self.group)

        self.attrs = STACKED_SPRITE_ATTRS[name]
        self.y_offset = vec2(0,self.attrs["y_offset"])
        self.cache = app.cache.stacked_sprite_cache
        self.viewing_angle = app.cache.viewing_angle
        self.rotated_sprite = self.cache[name]["rotated_sprites"]
        self.angle = 0
        self.screen_pos = vec2(0)
        self.rot = (rot % 360) // self.viewing_angle

    def transform(self):
        pos = self.pos - self.player.offset
        pos = pos.rotate_rad(self.player.angle)
        self.screen_pos = pos + CENTER

    def change_layer(self):
        self.group.change_layer(self, self.screen_pos.y)

    def get_angle(self):
        self.angle = -math.degrees(self.player.angle) // self.viewing_angle + self.rot
        self.angle = int(self.angle % NUM_ANGLES)

    def update(self):
        self.transform()
        self.get_angle()
        self.get_image()
        self.change_layer()

    def get_image(self):
        self.image = self.rotated_sprite[self.angle]
        self.rect = self.image.get_rect(center = self.screen_pos + self.y_offset)
