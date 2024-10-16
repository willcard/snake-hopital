import conf
from grid import Grid

class Game:
    def __init__(self) -> None:
        self.grid = Grid(conf.GRID_SHAPE)

    def run(self) -> None:
        print(self.grid.pretty_print())
        self.grid.snake.move('UP')
        print(self.grid.snake_is_out())