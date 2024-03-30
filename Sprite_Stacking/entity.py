from settings import *

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, app, name):
        self.app = app
        self.name = name
        self.group = app.main_group
        super().__init__(self.group)

        self.attrs = ENTITY_SPRITE_ATTRS[name]
        entity_cache = self.app.cache.entity_sprite_cache
        self.images = entity_cache[name]["images"]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.frame_index = 0