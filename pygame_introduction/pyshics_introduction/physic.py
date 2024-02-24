import pygame, sys, pymunk

def create_apple(space,pos:tuple):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 80)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    global screen
    for apple in apples:
        x = int(apple.body.position.x)
        y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0), (x,y), 80)

def static_ball(space, pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_static_balls(balls):
    global screen
    for ball in balls:
        x = int(ball.body.position.x)
        y = int(ball.body.position.y)
        pygame.draw.circle(screen,(100,100,100), (x,y), 50)


pygame.init()
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)
apples = []
apples.append(create_apple(space,(400,0)))
balls = []

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("app")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_RIGHT:
                balls.append(static_ball(space,event.pos))
            else:
                apples.append(create_apple(space,event.pos))
    screen.fill((217,217,217))
    draw_apples(apples)
    draw_static_balls(balls)
    space.step(1/50)
    pygame.display.flip()
    clock.tick(60)