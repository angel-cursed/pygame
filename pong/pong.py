import pygame, sys,random

class Block(pygame.sprite.Sprite):
    def __init__(self,path,x,y):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x,y))

class Player(Block):
    def __init__(self,path,x,y,speed):
        super().__init__(path,x,y)
        self.speed = speed
        self.movement = 0

    def screen_constraint(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constraint()

class Ball(Block):
    def __init__(self,path,x,y,speed_x,speed_y, paddles):
        super().__init__(path,x,y)
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
            pygame.mixer.Sound.play(ball_sound)

        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(ball_sound)
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1

    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((1,-1))
        self.speed_y *= random.choice((1,-1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (screen_widht/2, screen_height/2)
        pygame.mixer.Sound.play(score_sound)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time > 700:
            countdown_number = 3
        if 700 < current_time - self.score_time < 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time < 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = game_font.render(str(countdown_number), True, accent_color)
        time_counter_rect = time_counter.get_rect(center=(screen_widht/2, screen_height/2 + 50))
        pygame.draw.rect(screen, bg_color, time_counter_rect)
        screen.blit(time_counter, time_counter_rect)

class Opponent(Block):
    def __init__(self,path,x,y,speed):
        super().__init__(path,x,y)
        self.speed = speed

    def update(self,ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.top += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.bottom -= self.speed
        self.constraint()

    def constraint(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_widht:
            self.rect.top = screen_widht

class Game_Manager():
    def __init__(self, ball_group,paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right > screen_widht:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left < 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = game_font.render(str(self.player_score), True, accent_color)
        opponent_score = game_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft = (screen_widht/2 + 40, screen_height/2))
        opponent_score_rect = opponent_score.get_rect(midright=(screen_widht/2 - 40, screen_height/2))


        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)

#General Setup
pygame.init()
clock = pygame.time.Clock()

#SMain Window
screen_widht = 1280
screen_height = 760
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("Pong")

#Game Rectangles
player = Player("paddle.png",screen_widht - 20,screen_height/2,5)
opponent = Opponent("paddle.png",20, screen_height/2,5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)
middle_strip = pygame.Rect(screen_widht/2 - 2, 0,4,screen_height)

ball = Ball("ball.png",screen_widht/2,screen_height/2,5,5,paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = Game_Manager(ball_sprite,paddle_group)

#Colors
bg_color = pygame.Color('#2F373F')
accent_color = (27,35,43)

#Games Variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

#Score Timer
score_time = True

#Sounds
score_sound = pygame.mixer.Sound("score.ogg")
ball_sound = pygame.mixer.Sound("pong.ogg")

while True:
    #Handling Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
            if event.key == pygame.K_UP:
                player.movement -= player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
            if event.key == pygame.K_UP:
                player.movement += player.speed

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, accent_color, middle_strip)

    game_manager.run_game()

    #Updating the window
    pygame.display.flip()
    clock.tick(120)