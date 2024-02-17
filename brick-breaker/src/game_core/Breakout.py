import pygame, sys, random
class Breakout:
    def __init__(self, button_class, dir_class):

        # Core Attributes
        self.clock = pygame.time.Clock()
        self.button = button_class
        self.Dir = dir_class()
        self.screen_width = 1280
        self.screen_height = 760
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Brick Breaker")

        # Components
        self.ball = pygame.Rect((self.screen_width / 2 - 15, self.screen_height / 2 - 15), (30, 30))
        self.player = pygame.Rect((self.screen_width / 2 - 80, self.screen_height - 20), (160, 10))
        self.bricks = []
        self.bricks_color = []
        self.color_for_the_bricks = ["#8B8090", "#B698C2", "#DBB37F", "#C98486"]
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)
        self.end_font = pygame.font.Font("freesansbold.ttf", 64)
        self.restart_button = self.button("Restart", 440, 140, (self.screen_width /2 - 220,self.screen_height /2 - 100), self.color_for_the_bricks[2], self.color_for_the_bricks[3], self.color_for_the_bricks[1], self.color_for_the_bricks[0], self, 20)
        self.quit_button = self.button("Quit", 440, 140, (self.screen_width /2 - 220,self.screen_height /2 + 100), self.color_for_the_bricks[2], self.color_for_the_bricks[3], self.color_for_the_bricks[1], self.color_for_the_bricks[0], self, 20)

        # Sound
        self.song = pygame.mixer.Sound(self.Dir.SOUND / "breakout_song.mp3")
        self.lose_sound = pygame.mixer.Sound(self.Dir.SOUND / "lose.wav")
        self.success_sound = pygame.mixer.Sound(self.Dir.SOUND / "success.wav")
        self.brick_sound = pygame.mixer.Sound(self.Dir.SOUND / "brick.wav")
        self.ball_sound = pygame.mixer.Sound(self.Dir.SOUND / "beep.ogg")

        # Game Variables
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.player_speed = 0
        self.score = 0
        self.score_time = True
        self.choice = True

        # Bricks
        self.create_bricks()

        # Colors
        self.player_color = "#A499A5"
        self.ball_color = "#5F536C"
        self.bg_color = "#D9DBDA"
        self.font_color = self.player_color

        # Play Music
        self.song.play(loops = -1)

    def check_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player_speed -= 10
                if event.key == pygame.K_RIGHT:
                    self.player_speed += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player_speed += 10
                if event.key == pygame.K_RIGHT:
                    self.player_speed -= 10

    def create_bricks(self):
        self.bricks.clear()
        self.bricks_color.clear()
        distance = 40
        for i in range(32):
            if i <= 7:
                rect = pygame.Rect((distance, 20), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[0])
                distance += 150
            elif i == 8:
                distance = 40
                rect = pygame.Rect((distance, 60), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[1])
                distance += 150
            elif i <= 15:
                rect = pygame.Rect((distance, 60), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[1])
                distance += 150
            elif i == 16:
                distance = 40
                rect = pygame.Rect((distance, 100), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[2])
                distance += 150
            elif i <= 23:
                rect = pygame.Rect((distance, 100), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[2])
                distance += 150
            elif i == 24:
                distance = 40
                rect = pygame.Rect((distance, 140), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[3])
                distance += 150
            else:
                rect = pygame.Rect((distance, 140), (140, 30))
                self.bricks.append(rect)
                self.bricks_color.append(self.color_for_the_bricks[3])
                distance += 150


    def bricks_animation(self):
        for brick in self.bricks:
            if self.ball.colliderect(brick):
                if abs(self.ball.top - brick.bottom) < 10 or abs(self.ball.bottom - brick.top) < 10:
                    self.ball_speed_y *= -1
                    self.bricks_color.pop(self.bricks.index(brick))
                    self.bricks.remove(brick)
                    self.score += 1
                    self.brick_sound.play()
                elif abs(self.ball.right - brick.left) < 10 or abs(self.ball.left - brick.right) < 10:
                    self.ball_speed_x *= -1
                    self.bricks_color.pop(self.bricks.index(brick))
                    self.bricks.remove(brick)
                    self.score += 1
                    self.brick_sound.play()

        if len(self.bricks) == 0:
            self.success_sound.play()
            self.create_bricks()

    def player_animation(self):
        if self.player.right > self.screen_width:
            self.player.right = self.screen_width
        if self.player.left < 0:
            self.player.left = 0

        self.player.x += self.player_speed

    def ball_animation(self):
        if self.ball.colliderect(self.player):
            if abs(self.ball.right - self.player.left) < 10 and self.ball_speed_x > 0:
                self.ball_speed_x *= -1
                self.ball_sound.play()
            if abs(self.ball.left - self.player.right) < 10 and self.ball_speed_x < 0:
                self.ball_speed_x *= -1
                self.ball_sound.play()
            if abs(self.ball.bottom - self.player.top) < 10 and self.ball_speed_y > 0:
                self.ball_speed_y *= -1
                self.ball_sound.play()

        if self.ball.right >= self.screen_width and self.ball_speed_x > 0:
            self.ball_speed_x *= -1
            self.ball_sound.play()
        if self.ball.left <= 0 and self.ball_speed_x < 0:
            self.ball_speed_x *= -1
            self.ball_sound.play()
        if self.ball.top <= 0 and self.ball_speed_y < 0:
            self.ball_speed_y *= -1
            self.ball_sound.play()
        if self.ball.bottom >= self.screen_height:
            self.ball.center = (self.screen_width / 2, self.screen_height / 2)
            self.ball_speed_x = 0
            self.ball_speed_y = 0
            self.end_game()

        self.ball.y += self.ball_speed_y
        self.ball.x += self.ball_speed_x

    def draw(self):
        self.screen.fill("#D9DBDA")

        pygame.draw.ellipse(self.screen, "#5F536C", self.ball)
        pygame.draw.rect(self.screen, "#A499A5", self.player)

        for rect in self.bricks:
            pygame.draw.rect(self.screen, self.bricks_color[self.bricks.index(rect)], rect)

        score_text = self.game_font.render(f"{self.score}",False, self.font_color)
        self.screen.blit(score_text, (self.screen_width / 2 - 23, self.screen_height / 2 - 60))

        if self.score_time:
            self.screen.blit(self.text_number, (self.screen_width/2 - 23,self.screen_height/2 + 60))

        if self.choice is None:
            dark_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
            dark_surface.fill((0, 0, 0, 128))
            self.screen.blit(dark_surface, (0, 0))
            end_text = self.end_font.render("Game Over", True, (255, 255, 255))
            self.screen.blit(end_text, (self.screen_width / 2 - 200, self.screen_height / 2 - 300))

            end_text = self.end_font.render(f"Your Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(end_text, (self.screen_width / 2 - 200, self.screen_height / 2 - 250))
            self.restart_button.draw()
            self.quit_button.draw()



        pygame.display.flip()

    def new_round(self):
        current_time = pygame.time.get_ticks()
        self.ball.center = (self.screen_width/2, self.screen_height/2)

        if current_time - self.score_time < 700:
            self.text_number = self.game_font.render(f"3",False, self.font_color)

        elif 700 < current_time - self.score_time < 1400:
            self.text_number = self.game_font.render(f"2",False, self.font_color)

        elif 1400 < current_time - self.score_time < 2100:
            self.text_number = self.game_font.render(f"1",False, self.font_color)

        if current_time - self.score_time < 2100:
            self.ball_speed_x, self.ball_speed_y = 0,0
            self.ball.center = (self.screen_width/2 - 15,self.screen_height/2 - 15)
        else:
            self.ball_speed_x = 7 * random.choice((1,-1))
            self.ball_speed_y = 7 * random.choice((1,-1))
            self.score_time = None

    def end_game(self):
        self.ball.center = (self.screen_width/2,self.screen_height/2)
        self.choice = None
        self.lose_sound.play(loops = 0)
        while self.choice == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.restart_button.click_time and not self.quit_button.click_time:
                self.choice = self.restart_button.clicked()
            if self.quit_button.click_time and not self.restart_button.click_time:
                self.choice = self.quit_button.clicked()


            self.draw()

        if self.choice == "Quit":
            pygame.quit()
            sys.exit()

        self.score = 0
        self.score_time = pygame.time.get_ticks()
        self.choice = True
        self.restart_button.click_time = None
        self.create_bricks()
        self.player_speed = 0