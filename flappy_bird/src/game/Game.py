import pygame, sys, random, json

class Game():
    def __init__(self, screen_width, screen_height, screen, clock, path, player, pipe, phases, button):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.clock = clock
        self.Path = path()
        self.button = button
        self.Pipe = pipe
        self.can_spawn_pipe = True
        self.world_shift = 4
        self.score = 0
        self.phases = phases()
        self.phase = self.phases.MENU_PHASE

        self.bg = pygame.image.load(self.Path.ASSETS / "background.png")
        self.player = pygame.sprite.GroupSingle(player(self.Path.ASSETS / "player.png", (self.screen_width/2, self.screen_height/2), self.screen_width, self.screen_height))
        self.pipes = pygame.sprite.Group()
        self.pipes_movements = False
        self.pipes_spawn_time = (1500,2500)

        self.font = pygame.font.Font(self.Path.FONT / "font.ttf", 64)
        self.menu_font = pygame.font.Font(self.Path.FONT / "font.ttf", 45)
        self.title_font = pygame.font.Font(self.Path.FONT / "font.ttf", 90)

        self.play_button = self.button((self.screen_width/2, self.screen_height/2 + 78), self.Path.ASSETS / "button_play.png", self.Path.ASSETS / "button_play_clicked.png", self, "Play")
        self.quit_button = self.button((self.screen_width/2, self.screen_height/2 + 228), self.Path.ASSETS / "button_quit.png", self.Path.ASSETS / "button_quit_clicked.png", self, "Quit")
        self.menu_choice = None

    def collide_pipes(self):
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.pipes, False, pygame.sprite.collide_mask):
            self.restart_game()

    def screen_collisions(self):
        player = self.player.sprite
        if player.rect.bottom >= self.screen_height:
            self.restart_game()
        elif player.rect.top <= 0:
            self.restart_game()

    def check_score(self):
        for pipe in self.pipes.sprites():
            if -4 < self.player.sprite.rect.center[0] - pipe.rect.center[0] < 4:
                self.score += 0.5

    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.bg, (0, 0))
        self.pipes.draw(self.screen)
        self.player.draw(self.screen)
        if self.phase == self.phases.GAME_PHASE:
            score_text = self.font.render(f"{int(self.score)}", False, (255,255,255))
            self.screen.blit(score_text, (self.screen_width / 2 - 22, self.screen_height / 2 - 96))
        else:
            title_text = self.title_font.render("Flappy Bird", False, (255,255,255))
            self.screen.blit(title_text, (self.screen_width/2 - 165, self.screen_height/ 2 - 300))
            high_score_text = self.menu_font.render(f"Your Highest Score: {self.high_score}", False, (255,255,255))
            self.screen.blit(high_score_text, (self.screen_width/2 - 165, self.screen_height/ 2 - 150))
            self.play_button.draw()
            self.quit_button.draw()

    def import_high_score(self):
        with open(self.Path.JSON / "high_score.json") as f:
            self.high_score = json.load(f)["score"]

    def restart_game(self):
        self.import_high_score()
        if self.high_score < self.score:
            with open(self.Path.JSON / "high_score.json", "w") as f:
                json.dump({"score": int(self.score)}, f, indent=3)
        self.score = 0
        self.phase = self.phases.MENU_PHASE

    def difficulty_of_pipes(self):
        if self.score < 15:
            pipes_possibilities = [(250, 300), (100, 150), (350, 400)]
            self.pipes_spawn_time = (1500,2500)
            self.pipes_movements = False
        elif 15 <= self.score < 30:
            pipes_possibilities = [(300, 300), (150, 150), (400, 400)]
            self.pipes_movements = False
            self.pipes_spawn_time = (1500,2000)
        elif 30 <= self.score < 60:
            pipes_possibilities = [(250, 300), (100, 150), (350, 400)]
            self.pipes_movements = True
            self.pipes_spawn_time = (1000,2000)
        elif 60 <= self.score < 75:
            pipes_possibilities = [(300, 300), (150, 150), (400, 400)]
            self.pipes_movements = True
        else:
            pipes_possibilities = [(300, 300), (150, 150), (400, 400)]
            self.pipes_movements = True
            self.pipes_spawn_time = (1000,1500)
        return random.choice(pipes_possibilities)



    def spawn_pipes(self):
        if self.can_spawn_pipe == True:
            self.can_spawn_pipe = False
            pipe_height = self.difficulty_of_pipes()
            self.pipes.add(self.Pipe(self.Path.ASSETS / "pipe.png", False, (self.screen_width + 100, self.screen_height - pipe_height[0])))
            self.pipes.add(self.Pipe(self.Path.ASSETS / "pipe.png", True, (self.screen_width + 100, 0 - pipe_height[1])))
            self.delay = random.randint(1500,2500)

        elif self.can_spawn_pipe:
            if pygame.time.get_ticks() - self.can_spawn_pipe >= self.delay:
                self.can_spawn_pipe = True

        else:
            self.can_spawn_pipe = pygame.time.get_ticks()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.phase == self.phases.GAME_PHASE:
                self.spawn_pipes()
                self.player.update(pygame.event.get())
                self.pipes.update(self.world_shift, self.pipes_movements)
                self.collide_pipes()
                self.screen_collisions()
                self.check_score()
            elif self.phase == self.phases.MENU_PHASE:
                self.import_high_score()
                self.player.sprite.direction = 0
                for pipe in self.pipes.sprites():
                    pipe.kill()
                self.player.sprite.rect.center = (self.screen_width/2, self.screen_height/2 - 50)
                if self.play_button.click_time and not self.quit_button.click_time:
                    self.menu_choice = self.play_button.clicked()
                if self.quit_button.click_time and not self.play_button.click_time:
                    self.menu_choice = self.quit_button.clicked()
                if self.menu_choice:
                    if self.menu_choice == "Play":
                        self.phase = self.phases.GAME_PHASE
                        self.menu_choice = None
                        self.score = 0
                    elif self.menu_choice == "Quit":
                        pygame.quit()
                        sys.exit()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)