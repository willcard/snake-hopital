import conf
from grid import Grid
import pygame
import time

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((400, 300))
        pygame.init()

        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

    def start(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.grid.snake_move('UP')
                    elif event.key == pygame.K_DOWN:
                        self.grid.snake_move('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.grid.snake_move('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.grid.snake_move('RIGHT')
                    print(self.grid.pretty_print())
                    #time.sleep(0.5)