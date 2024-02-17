import pygame

class Button():
    def __init__(self, text, width, height, position: tuple, top_color, bottom_color, over_color, text_color, game, elevation):

        #Core Attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y = position[1]
        self.text = text
        self.click_time = None
        self.game = game

        #top rectangle
        self.top_rect = pygame.Rect(position,(width, height))
        self.top_color = top_color
        self.dynamic_top_color = top_color

        #bottom rectangle
        self.bottom_rect = pygame.Rect(position,(width, height))
        self.bottom_color = bottom_color

        #text
        self.text_color = text_color
        self.text_surface = self.game.end_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)
        self.over_color = over_color

    def draw(self):

        #elevation logic
        self.top_rect.y = self.original_y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        pygame.draw.rect(self.game.screen, self.bottom_color, self.bottom_rect, border_radius = 25)
        pygame.draw.rect(self.game.screen, self.dynamic_top_color, self.top_rect, border_radius = 25)
        self.game.screen.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.dynamic_top_color = self.over_color
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            elif self.pressed:
                self.dynamic_elevation = self.elevation
                self.pressed = False
                self.click_time = pygame.time.get_ticks()
                self.clicked()
        else:
            self.dynamic_elevation = self.elevation
            self.dynamic_top_color = self.top_color

    def clicked(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.click_time >= 500:
            return self.text
        else:
            return None
