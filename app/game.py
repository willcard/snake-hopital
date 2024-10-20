import conf
from grid import Grid
import pygame
import time

class Game:
    LINE_COLOR = (125, 125, 125)
    BG_COLOR = (0, 0, 0)
    SNAKE_COLOR = (83, 157, 85)
    APPLE_COLOR = (255, 0, 0)
    CELL_WIDTH = 30

    def __init__(self) -> None:
        pygame.init()

        self.n_rows = conf.GRID_SHAPE[0]
        self.n_cols = conf.GRID_SHAPE[1]

        self.screen_width = self.n_rows*self.CELL_WIDTH
        self.screen_height = self.n_cols*self.CELL_WIDTH
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))

        self.speed = conf.SPEED
        self.grid = Grid(self.n_rows, self.n_cols)


    def start(self) -> None:
        """
            Main game loop: get pressed key and update game.
        """
        #print(self.grid.pretty_print())

        last_event = 'DOWN'
        game_is_ok = True
        while game_is_ok:
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
            
            #print(self.grid.pretty_print())
            self.update_screen()

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
                pygame.draw.rect(self.screen, color, (col * self.CELL_WIDTH, row * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH))
                pygame.draw.rect(self.screen, self.LINE_COLOR, (col * self.CELL_WIDTH, row * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH), 1)

    def update_screen(self) -> None:
        """
            Update screen for each step.
        """
        self.screen.fill(self.BG_COLOR)
        self.draw_grid()
        pygame.display.flip()