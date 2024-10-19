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
        while True:
            LAST_EVENT = 'DOWN'
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        LAST_EVENT = 'UP'
                    elif event.key == pygame.K_DOWN:
                        LAST_EVENT = 'DOWN'
                    elif event.key == pygame.K_LEFT:
                        LAST_EVENT = 'LEFT'
                    elif event.key == pygame.K_RIGHT:
                        LAST_EVENT = 'RIGHT'
            
            self.grid.snake_move(LAST_EVENT)
            print(self.grid.pretty_print())
            time.sleep(self.speed)