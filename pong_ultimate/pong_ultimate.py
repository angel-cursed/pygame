import pygame, sys,random

class Pong():


    def __init__(self, screen_widht, screen_height):
        self.screen_widht = screen_widht
        self.screen_height = screen_height
        self.chosed_button = None
        self.dt = 0
        self.last_frame_ticks = 0

        #Game Rectangles
        self.ball = pygame.Rect(screen_widht/2 - 15, screen_height/2 - 15, 30, 30)
        self.player = pygame.Rect(screen_widht - 20, screen_height/2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

        #Game Mode
        self.game_mode = None

        # Colors
        self.bg_color = (41, 163, 41)
        self.yellow = (255, 255, 0)

        #Games Variables
        self.ball_speed_x = 7 * random.choice((1,-1))
        self.ball_speed_y = 7 * random.choice((1,-1))
        self.player_speed = 0

        #Text Variables
        self.player_score = 0
        self.opponent_score = 0
        self.game_font = pygame.font.Font("freesansbold.ttf",32)

        #Score Timer
        self.score_time = True

        #Sounds
        self.score_sound = pygame.mixer.Sound("score.ogg")
        self.ball_sound = pygame.mixer.Sound("pong.ogg")

    def ball_animation(self):

        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            pygame.mixer.Sound.play(self.ball_sound)
            self.ball_speed_y *= -1

        if self.ball.left <= 0:
            pygame.mixer.Sound.play(self.score_sound)
            self.player_score += 1
            self.score_time = pygame.time.get_ticks()

        if self.ball.right >= screen_width:
            pygame.mixer.Sound.play(self.score_sound)
            self.opponent_score += 1
            self.score_time = pygame.time.get_ticks()

        if self.ball.colliderect(self.player) and self.ball_speed_x > 0:
            pygame.mixer.Sound.play(self.ball_sound)
            if abs(self.ball.right - self.player.left) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.top - self.player.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.bottom - self.player.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1


        if self.ball.colliderect(self.opponent) and self.ball_speed_x < 0:
            pygame.mixer.Sound.play(self.ball_sound)
            if abs(self.ball.left - self.opponent.right) < 10:
                self.ball_speed_x *= -1
            elif abs(self.ball.top - self.opponent.bottom) < 10 and self.ball_speed_y < 0:
                self.ball_speed_y *= -1
            elif abs(self.ball.bottom - self.opponent.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1

    def player_animation(self):

        self.player.y += self.player_speed
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= screen_height:
            self.player.bottom = screen_height

    def opponent_animation(self):

        self.opponent.y += self.opponent_speed
        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= screen_height:
            self.opponent.bottom = screen_height

    def opponent_ai(self):

        if self.opponent.top < self.ball.y:
            self.opponent.top += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.bottom -= self.opponent_speed
        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= screen_height:
            self.opponent.bottom = screen_height

    def ball_restart(self):

        current_time = pygame.time.get_ticks()
        self.ball.center = (screen_width / 2, screen_height / 2)

        if current_time - self.score_time < 700:
            number_three = self.game_font.render("3",False,self.yellow)
            number_rect = number_three.get_rect(center = (screen_width / 2, screen_height / 2 + 50))
            pygame.draw.rect(screen, self.bg_color, number_rect)
            screen.blit(number_three, number_rect)

        if 700 < current_time - self.score_time < 1400:
            number_two = self.game_font.render("2",False,self.yellow)
            number_rect = number_two.get_rect(center = (screen_width / 2, screen_height / 2 + 50))
            pygame.draw.rect(screen, self.bg_color, number_rect)
            screen.blit(number_two, number_rect)

        if 1400 < current_time - self.score_time < 2100:
            number_one = self.game_font.render("1",False,self.yellow)
            number_rect = number_one.get_rect(center = (screen_width / 2, screen_height / 2 + 50))
            pygame.draw.rect(screen, self.bg_color, number_rect)
            screen.blit(number_one, number_rect)

        if current_time - self.score_time < 2100:
            self.ball_speed_x,self.ball_speed_y = 0,0
        else:
            self.ball_speed_y = 7 * random.choice((1, -1))
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.score_time = None

    def set_mode(self,mode):
        self.game_mode = mode
        if mode == "solo":
            self.opponent_speed = 7
        else:
            self.opponent_speed = 0

    def pause_menu(self):

        button_resume = button("Resume", 200, 100, (screen_width / 2 - 100, screen_height / 2 - 300), 10)
        button_quit = button("Quit", 200, 100, (screen_width / 2 - 100, screen_height / 2 - 150), 10)
        button_change_mode = button("Gamemode", 200, 100, (screen_width / 2 - 100, screen_height / 2), 10)
        button_restart = button("Restart", 200, 100, (screen_width / 2 - 100, screen_height / 2 + 150), 10)

        self.button_chosen = None

        while self.button_chosen is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if button_quit.click_time:
                button_quit.clicked()
            if button_restart.click_time:
                button_restart.clicked()
            if button_change_mode.click_time:
                button_change_mode.clicked()
            if button_resume.click_time:
                button_resume.clicked()

            # Visuals
            screen.fill(game.bg_color)
            pygame.draw.rect(screen, game.yellow, game.player)
            pygame.draw.rect(screen, game.yellow, game.opponent)
            pygame.draw.ellipse(screen, game.yellow, game.ball)
            pygame.draw.aaline(screen, game.yellow, (screen_width / 2, 0), (screen_width / 2, screen_height))

            player_text = game.game_font.render(f"{game.player_score}", False, game.yellow)
            screen.blit(player_text, (screen_width / 2 + 20, screen_height / 2))

            opponent_text = game.game_font.render(f"{game.opponent_score}", False, game.yellow)
            screen.blit(opponent_text, (screen_width / 2 - 40, screen_height / 2))

            dark_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
            dark_surface.fill((0, 0, 0, 128))
            screen.blit(dark_surface, (0, 0))

            button_resume.draw()
            button_quit.draw()
            button_change_mode.draw()
            button_restart.draw()

            # Updating the window
            pygame.display.flip()
            clock.tick(60)

        if self.button_chosen == button_quit.text:
            pygame.quit()
            sys.exit()
        elif self.button_chosen == button_change_mode.text:
            self.change_gamemode()
        elif self.button_chosen == button_restart.text:
            self.player_score, game.opponent_score = 0, 0
            self.score_time = pygame.time.get_ticks()
            self.ball_restart()

    def change_gamemode(self):
        button_solo = button("Solo Mode", 200, 100, (screen_width / 2 - 300, screen_height / 2 - 50), 10)
        button_duo = button("Duo Mode", 200, 100, (screen_width / 2 + 100, screen_height / 2 - 50), 10)
        self.game_mode = None
        while self.game_mode is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if button_solo.click_time and not button_duo.click_time:
                button_solo.clicked()
            if button_duo.click_time and not button_solo.click_time:
                button_duo.clicked()
            screen.fill((136, 160, 168))
            button_solo.draw()
            button_duo.draw()
            pygame.display.update()
            clock.tick(60)
        self.player_score = 0
        self.opponent_score = 0
        self.score_time = pygame.time.get_ticks()
        self.ball_restart()

    def check_input(self):
        # Handling Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player_speed += 7
                if event.key == pygame.K_UP:
                    self.player_speed -= 7
                if self.game_mode == "duo":
                    if event.key == pygame.K_z:
                        self.opponent_speed -= 7
                    if event.key == pygame.K_s:
                        self.opponent_speed += 7
                if event.key == pygame.K_ESCAPE:
                    self.pause_menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player_speed -= 7
                if event.key == pygame.K_UP:
                    self.player_speed += 7
                if self.game_mode == "duo":
                    if event.key == pygame.K_z:
                        self.opponent_speed += 7
                    if event.key == pygame.K_s:
                        self.opponent_speed -= 7


class button():
    def __init__(self, text, width, height, position: tuple, elevation):

        #Core Attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y = position[1]
        self.text = text
        self.click_time = None

        #top rectangle
        self.top_rect = pygame.Rect(position,(width, height))
        self.top_color = game.bg_color

        #bottom rectangle
        self.bottom_rect = pygame.Rect(position,(width, height))
        self.bottom_color = game.yellow

        #text
        self.text_color = (56,77,72)
        self.text_surface = game.game_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def draw(self):

        #elevation logic
        self.top_rect.y = self.original_y - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 25)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 25)
        screen.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (146,220,229)
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
            self.top_color = game.bg_color

    def clicked(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.click_time >= 500:
            if self.text == "Solo Mode":
                game.set_mode("solo")
            elif self.text == "Duo Mode":
                game.set_mode("duo")
            else:
                game.button_chosen = self.text


#General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 760
pygame.display.set_caption("Pong Ultimate")
pygame.display.set_icon(pygame.image.load("pong_icon.png"))
screen = pygame.display.set_mode((screen_width, screen_height))


game = Pong(screen_width, screen_height)

game.change_gamemode()

while True:

    game.check_input()

    game.ball_animation()
    game.player_animation()
    if game.game_mode == "solo":
        game.opponent_ai()
    else:
        game.opponent_animation()

    #Visuals
    screen.fill(game.bg_color)
    pygame.draw.rect(screen,game.yellow,game.player)
    pygame.draw.rect(screen,game.yellow,game.opponent)
    pygame.draw.ellipse(screen,game.yellow,game.ball)
    pygame.draw.aaline(screen, game.yellow, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if game.score_time:
        game.ball_restart()

    player_text = game.game_font.render(f"{game.player_score}",False,game.yellow)
    screen.blit(player_text, (screen_width / 2 + 20, screen_height / 2))

    opponent_text = game.game_font.render(f"{game.opponent_score}",False,game.yellow)
    screen.blit(opponent_text, (screen_width / 2 - 40, screen_height / 2))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)
