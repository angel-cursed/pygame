import pygame
from game_core import Breakout, Button, Dir

pygame.init()
game = Breakout(Button, Dir)



while True:
    game.check_inputs()
    game.bricks_animation()
    game.player_animation()
    game.ball_animation()

    if game.score_time:
        if game.score_time == True:
            game.score_time = pygame.time.get_ticks()
        game.new_round()

    game.draw()

    game.clock.tick(60)

