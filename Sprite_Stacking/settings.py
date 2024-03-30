import pygame

vec2 = pygame.math.Vector2

RES = WIDTH, HEIGHT = vec2(1600,900)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
TILE_SIZE = 250

BG_COLOR = "olivedrab"
NUM_ANGLES = 90

PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015

ENTITY_SPRITE_ATTRS = {
    "player": {
        "path": "assets/entities/player/player.png",
        "num_layers": 7,
        "scale": 0.35,
        "y_offset": 0
    }
}

STACKED_SPRITE_ATTRS = {
    "grass": {
        "path": "assets/grass.png",
        "num_layers": 11,
        "scale": 7,
        "y_offset": -40,
        "outline": False
    },
    "blue_tree": {
        "path": "assets/blue_tree.png",
        "num_layers": 43,
        "scale": 8,
        "y_offset": -170
    },
    "car": {
        "path": "assets/car.png",
        "num_layers": 9,
        "scale": 10,
        "y_offset": -10
    },
    "van":{
        "path": "assets/van.png",
        "num_layers": 20,
        "scale": 6,
        "y_offset": -30
    },
    "tank":{
        "path": "assets/tank.png",
        "num_layers": 17,
        "scale": 8,
        "y_offset": -40
    }
}