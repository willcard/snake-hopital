import conf
from grid import Grid
import pygame
import time

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((400, 300))
        pygame.init()

        self.speed = conf.SPEED
        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

    def start(self) -> None:
        """
            Main game loop: get pressed key and update game.
        """
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
            print(self.grid.pretty_print())
            time.sleep(self.speed)