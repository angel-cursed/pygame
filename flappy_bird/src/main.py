import pygame
from game import *

pygame.init()
clock = pygame.time.Clock()

screen_width = 360
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
game = Game(screen_width, screen_height, screen, clock, Root, Player, Pipe, Phases, Button)

game.run()