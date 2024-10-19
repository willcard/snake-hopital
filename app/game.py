import conf
from grid import Grid

class Game:
    def __init__(self) -> None:
        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

    def run(self, move) -> None:
        self.grid.snake.move(move)
        self.grid.update()
        print(self.grid.pretty_print())