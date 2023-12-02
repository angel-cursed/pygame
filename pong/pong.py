import pygame, sys,random

def ball_animation():
    global ball_speed_x, ball_speed_y,opponent_score,player_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(ball_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_widht:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(ball_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1


    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(ball_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

def player_animation():

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():

    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x,ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_widht/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,yellow)
        screen.blit(number_three,(screen_widht/2 - 10,screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,yellow)
        screen.blit(number_two,(screen_widht/2 - 10,screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,yellow)
        screen.blit(number_one,(screen_widht/2 - 10,screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


#General Setup
pygame.init()
clock = pygame.time.Clock()

#SMain Window
screen_widht = 1280
screen_height = 760
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("Pong")

#Game Rectangles
ball = pygame.Rect(screen_widht/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_widht - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Colors
bg_color = (41, 163, 41)
#pygame.Color("grey12")
yellow = (255, 255, 0)

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
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,yellow,player)
    pygame.draw.rect(screen,yellow,opponent)
    pygame.draw.ellipse(screen,yellow,ball)
    pygame.draw.aaline(screen,yellow,(screen_widht/2,0),(screen_widht/2,screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}",False,yellow)
    screen.blit(player_text,(screen_widht/2 + 20,screen_height/2))

    opponent_text = game_font.render(f"{opponent_score}",False,yellow)
    screen.blit(opponent_text,(screen_widht/2 - 40,screen_height/2))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)