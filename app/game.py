import conf
from grid import Grid
import time

class Game:
    def __init__(self) -> None:
        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

        self.TEST_MOVES = ['DOWN','RIGHT','DOWN','RIGHT','DOWN','RIGHT','DOWN','RIGHT',
                           'UP','LEFT','UP','LEFT','UP','LEFT','UP','LEFT',
                           'DOWN','RIGHT','DOWN','RIGHT','DOWN','RIGHT','DOWN','RIGHT',
                           'UP','LEFT','UP','LEFT','UP','LEFT','UP','LEFT']


    def start(self) -> None:
        while self.TEST_MOVES:
            move = self.get_user_move()
            self.grid.snake_move(move)
            print(self.grid.pretty_print())
            time.sleep(0.5)

    def get_user_move(self) -> str:
        return self.TEST_MOVES.pop(0)