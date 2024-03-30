from settings import *
import math
from entity import BaseEntity

class Player(BaseEntity):
    def __init__(self, app, name = "player"):
        super().__init__(app, name)

        self.group.change_layer(self, CENTER.y)

        self.rect = self.image.get_rect(center = CENTER)

        self.offset = vec2(0)
        self.inc = vec2(0)
        self.dx, self.dy = 0, 0
        self.angle = 0
        self.diag_move_corr = 1 / math.sqrt(2)

    def control(self):
        self.inc = vec2(0)
        speed = PLAYER_SPEED * self.app.delta_time
        rot_speed = PLAYER_ROT_SPEED * self.app.delta_time

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.angle += rot_speed
        if key_state[pygame.K_RIGHT]:
            self.angle -= rot_speed

        if key_state[pygame.K_z]:
            self.inc += vec2(0, -speed).rotate_rad(-self.angle)
        if key_state[pygame.K_s]:
            self.inc += vec2(0, speed).rotate_rad(-self.angle)
        if key_state[pygame.K_q]:
            self.inc += vec2(-speed, 0).rotate_rad(-self.angle)
        if key_state[pygame.K_d]:
            self.inc += vec2(speed, 0).rotate_rad(-self.angle)

        if self.inc.x and self.inc.y:
            self.inc *= self.diag_move_corr

    def update(self):
        self.control()
        self.move()

    def move(self):
        self.offset += self.inc