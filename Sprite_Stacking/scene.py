from stacked_sprite import *
from random import uniform

P = "player"
A, B, C, D, E = "van", "tank", "blue_tree", "car", "grass"

MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, C, C, C, 0, C, C, 0, 0],
    [0, C, 0, 0, 0, 0, 0, C, 0],
    [C, 0, B, 0, C, E, 0, C, 0],
    [C, 0, E, 0, P, 0, E, C, 0],
    [C, 0, 0, A, E, D, C, C, 0],
    [0, C, 0, 0, 0, 0, C, C, 0],
    [0, C, C, 0, 0, 0, C, C, 0],
    [0, 0, 0, C, C, C, C, 0, 0],
]

MAP_SIZE = MAP_WIDTH, MAP_HEIGHT = vec2(len(MAP), len(MAP[0]))
MAP_CENTER = MAP_SIZE / 2

class Scene:
    def __init__(self, app):
        self.app = app
        self.load_scene()

    def load_scene(self):
        rand_rot = lambda : uniform(0, 360)
        rand_pos = lambda pos: pos + vec2(uniform(-0.25, 0.25))
        for j, row in enumerate(MAP):
            for i, name in enumerate(row):
                pos = vec2(i, j) + vec2(0.5)
                if name == P:
                    self.app.player.offset = pos * TILE_SIZE
                elif name:
                    StackedSprite(self.app, name = name, pos = rand_pos(pos), rot = rand_rot())