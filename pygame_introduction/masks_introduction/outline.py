import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

obstacle_surf = pygame.image.load("img.png").convert_alpha()
obstacle_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

#complex way to get an outline
new_obstacle_surf = obstacle_mask.to_surface()
new_obstacle_surf.set_colorkey((0,0,0))
new_obstacle_surf.fill('orange', special_flags=pygame.BLEND_RGBA_MULT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("grey")
    #complex way for an outline
    offset = 5
    screen.blit(new_obstacle_surf, (obstacle_pos[0] + offset, obstacle_pos[1])) #right
    screen.blit(new_obstacle_surf, (obstacle_pos[0] -offset, obstacle_pos[1])) #left
    screen.blit(new_obstacle_surf, (obstacle_pos[0], obstacle_pos[1] - offset)) #top
    screen.blit(new_obstacle_surf, (obstacle_pos[0], obstacle_pos[1] + offset)) #bottom
    screen.blit(new_obstacle_surf, (obstacle_pos[0] +offset, obstacle_pos[1] - offset)) #top right
    screen.blit(new_obstacle_surf, (obstacle_pos[0] +offset, obstacle_pos[1] + offset)) #bottom right
    screen.blit(new_obstacle_surf, (obstacle_pos[0] -offset, obstacle_pos[1] - offset)) #top left
    screen.blit(new_obstacle_surf, (obstacle_pos[0] -offset, obstacle_pos[1] + offset)) #bottom left
    screen.blit(obstacle_surf, obstacle_pos)

    #simple way for outline
    # for point in obstacle_mask.outline():
    #     x = point[0] + obstacle_pos[0]
    #     y = point[1] + obstacle_pos[1]
    #     pygame.draw.circle(screen, "red",(x,y), 5)

    pygame.display.flip()
    clock.tick(60)