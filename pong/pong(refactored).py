import pygame, sys,random

class Pong():

    def __init__(self, screen_widht, screen_height):
        self.screen_widht = screen_widht
        self.screen_height = screen_height

        #Game Rectangles
        self.ball = pygame.Rect(screen_widht/2 - 15, screen_height/2 - 15, 30, 30)
        self.player = pygame.Rect(screen_widht - 20, screen_height/2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

        # Colors
        self.bg_color = (41, 163, 41)
        # pygame.Color("grey12")
        self.yellow = (255, 255, 0)
        #Games Variables
        self.ball_speed_x = 7 * random.choice((1,-1))
        self.ball_speed_y = 7 * random.choice((1,-1))
        self.player_speed = 0
        self.opponent_speed = 7

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

        if self.ball.right >= screen_widht:
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
        self.ball.center = (screen_widht/2, screen_height/2)

        if current_time - self.score_time < 700:
            number_three = self.game_font.render("3",False,self.yellow)
            screen.blit(number_three,(screen_widht/2 - 10,screen_height/2 + 20))

        if 700 < current_time - self.score_time < 1400:
            number_two = self.game_font.render("2",False,self.yellow)
            screen.blit(number_two,(screen_widht/2 - 10,screen_height/2 + 20))

        if 1400 < current_time - self.score_time < 2100:
            number_one = self.game_font.render("1",False,self.yellow)
            screen.blit(number_one,(screen_widht/2 - 10,screen_height/2 + 20))

        if current_time - self.score_time < 2100:
            self.ball_speed_x,self.ball_speed_y = 0,0
        else:
            self.ball_speed_y = 7 * random.choice((1, -1))
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.score_time = None


#General Setup
pygame.init()
clock = pygame.time.Clock()

#SMain Window
screen_widht = 1280
screen_height = 760
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("Pong")

mode = None

while mode is None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(screen_widht/2 - 50,screen_height/2,50,50))
    pygame.draw.rect(screen,(255,255,255),(screen_widht/2 + 50,screen_height/2,50,50))
    pygame.display.update()
    clock.tick(60)

game = Pong(screen_widht, screen_height)

while True:
    #Handling Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                game.player_speed += 7
            if event.key == pygame.K_UP:
                game.player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                game.player_speed -= 7
            if event.key == pygame.K_UP:
                game.player_speed += 7

    game.ball_animation()
    game.player_animation()
    game.opponent_ai()
    #Visuals
    screen.fill(game.bg_color)
    pygame.draw.rect(screen,game.yellow,game.player)
    pygame.draw.rect(screen,game.yellow,game.opponent)
    pygame.draw.ellipse(screen,game.yellow,game.ball)
    pygame.draw.aaline(screen,game.yellow,(screen_widht/2,0),(screen_widht/2,screen_height))

    if game.score_time:
        game.ball_restart()

    player_text = game.game_font.render(f"{game.player_score}",False,game.yellow)
    screen.blit(player_text,(screen_widht/2 + 20,screen_height/2))

    opponent_text = game.game_font.render(f"{game.opponent_score}",False,game.yellow)
    screen.blit(opponent_text,(screen_widht/2 - 40,screen_height/2))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)