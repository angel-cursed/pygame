import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

player_surf = pygame.Surface((50,50))
player_surf.fill("red")
player_rect = player_surf.get_rect(center = (300,300))
player_mask = pygame.mask.from_surface(player_surf)

obstacle_surf = pygame.image.load("img.png").convert_alpha()
obstacle_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")

    screen.blit(obstacle_surf, obstacle_pos)

    if pygame.mouse.get_pos():
        player_rect.center = pygame.mouse.get_pos()
    screen.blit(player_surf,player_rect)


    offset_x = obstacle_pos[0] - player_rect.left
    offset_y = obstacle_pos[1] - player_rect.top
    # if player_mask.overlap(obstacle_mask,(offset_x, offset_y)):
    #     print(player_mask.overlap(obstacle_mask,(offset_x, offset_y)))

    if player_mask.overlap_area(obstacle_mask,(offset_x, offset_y)) >= 100:
        print(player_mask.overlap_area(obstacle_mask,(offset_x, offset_y)))

    pygame.display.flip()
    clock.tick(60)