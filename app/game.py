import conf
from grid import Grid

class Game:
    def __init__(self) -> None:
        self.grid = Grid(*conf.GRID_SHAPE)
        print(self.grid.pretty_print())

        self.TEST_MOVES = ['DOWN','DOWN','RIGHT','DOWN','RIGHT']


    def start(self) -> None:
        while self.TEST_MOVES:
            move = self.get_user_move()
            self.grid.snake_move(move)
            print(self.grid.pretty_print())

    def get_user_move(self) -> str:
        return self.TEST_MOVES.pop(0)