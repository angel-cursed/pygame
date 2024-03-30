import sys
from settings import *
from stacked_sprite import StackedSprite
from cache import Cache
from Player import Player
from scene import Scene

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.time = 0
        self.delta_time = 0.01

        self.main_group = pygame.sprite.LayeredUpdates()
        self.cache = Cache()
        self.player = Player(self)
        self.scene = Scene(self)


    def update(self):
        self.main_group.update()
        pygame.display.set_caption(f"{self.clock.get_fps(): .1f}")
        self.delta_time = self.clock.tick()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.main_group.draw(self.screen)
        pygame.display.flip()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.check_event()
            self.get_time()
            self.update()
            self.draw()

if __name__ == "__main__":
    app = App()
    app.run()