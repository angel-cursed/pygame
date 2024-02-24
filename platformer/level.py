import pygame
from settings import tile_size
from Tile import Tile
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for tile_index, tile in enumerate(row):
                if tile == "X":
                    x = tile_index * tile_size
                    y = row_index * tile_size
                    self.tiles.add(Tile((x, y), tile_size))
                elif tile == "P":
                    x = tile_index * tile_size
                    y = row_index * tile_size
                    self.player.add(Player((x, y)))

    def run(self):
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.player.draw(self.display_surface)