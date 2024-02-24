import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 760

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")
base_font = pygame.font.Font(None, 32)
user_text = ""

input_rect = pygame.Rect((200,200),(140,32))
color_active = pygame.Color("lightskyblue3")
color_inactive = pygame.Color("gray15")
color = color_inactive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_inactive


        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode

    screen.fill("black")

    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(text_surface.get_width() + 10, 100)

    pygame.display.flip()
    clock.tick(60)