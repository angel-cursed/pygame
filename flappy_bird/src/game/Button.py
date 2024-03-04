import pygame

class Button():
    def __init__(self, position: tuple, image, clicked_image, game, value):

        #Core Attributes
        self.pressed = False
        self.click_time = None
        self.game = game
        self.value = value

        #top rectangle
        self.image = pygame.image.load(image)
        self.clicked_image = pygame.image.load(clicked_image)
        self.dynamic_image = self.image
        self.rect = self.image.get_rect(center = position)


    def draw(self):
        self.game.screen.blit(self.dynamic_image, self.rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_image = self.clicked_image
                self.pressed = True
            elif self.pressed:
                self.dynamic_image = self.image
                self.pressed = False
                self.click_time = pygame.time.get_ticks()
                self.clicked()

    def clicked(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.click_time >= 500:
            self.click_time = None
            return self.value
        else:
            return None
