import conf
from grid import Grid
import pygame
import time
import logging

class Game:
    TITLE = 'Snake Hopital'
    TEXT_COLOR = (255, 255, 255)
    LINE_COLOR = (125, 125, 125)
    BG_COLOR = (0, 0, 0)
    SNAKE_COLOR = (83, 157, 85)
    APPLE_COLOR = (255, 0, 0)

    FONT_SIZE = 36
    CELL_WIDTH = 30
    STATS_PADDING_HEIGHT = 50

    INITIAL_SPEED = 1

    LOG_LEVEL = logging.DEBUG

    def __init__(self) -> None:
        pygame.init()

        self.n_rows = conf.GRID_SHAPE[0]
        self.n_cols = conf.GRID_SHAPE[1]

        self.screen_width = self.n_rows*self.CELL_WIDTH
        self.screen_height = self.n_cols*self.CELL_WIDTH
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height + self.STATS_PADDING_HEIGHT))
        
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)
        pygame.display.set_caption(self.TITLE)

        self.speed = self.INITIAL_SPEED
        self.grid = Grid(self.n_rows, self.n_cols)

        self.stats = dict()
        self.update_stats()
        
        self.logger = logging.getLogger()
        self.logger.setLevel(self.LOG_LEVEL)
        self.logger.addHandler(logging.StreamHandler())


    def start(self) -> None:
        """
            Main game loop: get pressed key and update game.
        """

        last_event = 'DOWN'
        game_is_ok = True
        while game_is_ok:
            self.log_stats()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        last_event = 'UP'
                    elif event.key == pygame.K_DOWN:
                        last_event = 'DOWN'
                    elif event.key == pygame.K_LEFT:
                        last_event = 'LEFT'
                    elif event.key == pygame.K_RIGHT:
                        last_event = 'RIGHT'
            
            game_is_ok = self.grid.snake_move(last_event)
            
            self.update_screen()
            self.update_speed()
            self.update_stats()

            time.sleep(self.speed)

    def draw_grid(self) -> None:
        """
            Draw game grid on screen.
        """
        grid_values = self.grid.get_grid_values()

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if grid_values[row][col] == self.grid.snake.MARKER:
                    color = self.SNAKE_COLOR
                elif grid_values[row][col] == self.grid.apple.MARKER:
                    color = self.APPLE_COLOR
                else:
                    color = self.BG_COLOR
                pygame.draw.rect(self.screen, color, 
                                 (col * self.CELL_WIDTH, 
                                  row * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH))
                pygame.draw.rect(self.screen, self.LINE_COLOR, 
                                 (col * self.CELL_WIDTH, 
                                  row * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH), 1)

    def write_infos(self) -> None:
        """
            Write infos on screen.
        """
        infos = f"Score: {self.stats['Score']}"
        text = self.font.render(infos, True, self.TEXT_COLOR)

        text_rect = text.get_rect(centerx=self.screen.get_width() // 2)
        text_rect.y = self.screen.get_height() - text_rect.height - 10 

        self.screen.blit(text, text_rect)


    def update_screen(self) -> None:
        """
            Update screen for each step.
        """
        self.screen.fill(self.BG_COLOR)
        self.draw_grid()
        self.write_infos()

        pygame.display.flip()

    def update_speed(self) -> None:
        """
            Update speed based on snake's length.
        """
        length = self.grid.snake.get_length()
        coef = length//2 +1
        new_speed = self.INITIAL_SPEED - (coef*0.1)

        if new_speed > 0.2:
            self.speed = new_speed

    def update_stats(self) -> None:
        """
            Update games' stats for each step.
        """
        self.stats = {'Score':self.grid.snake.get_length(),
                      'Speed':round(self.speed,1)}

    def log_stats(self) -> None:
        """
            Log games stats and grid view in terminal.
        """
        pretty_stats = " | ".join([f"{s} : {v}" for s,v in self.stats.items()])
        pretty_grid = self.grid.pretty_print()

        self.logger.info(pretty_stats)
        self.logger.info(pretty_grid)
