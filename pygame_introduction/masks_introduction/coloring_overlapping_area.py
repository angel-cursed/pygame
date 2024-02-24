import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

ship_surf = pygame.image.load("ship1.png")
ship_rect = ship_surf.get_rect(center = (300,300))
ship_mask = pygame.mask.from_surface(ship_surf)

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
        ship_rect.center = pygame.mouse.get_pos()

    screen.blit(ship_surf, ship_rect)

    #NEW MASK SURFACE COLORING
    offset_x = obstacle_pos[0] - ship_rect.left
    offset_y = obstacle_pos[1] - ship_rect.top

    if ship_mask.overlap(obstacle_mask, (offset_x,offset_y)):
        new_mask = ship_mask.overlap_mask(obstacle_mask, (offset_x,offset_y))
        new_surf = new_mask.to_surface()
        new_surf.set_colorkey((0,0,0))
        new_surf.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(new_surf,ship_rect)

    pygame.display.flip()
    clock.tick(60)