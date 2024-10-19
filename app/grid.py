from components import Snake, Apple

class Grid:
    def __init__(self, width:int =10, height:int =10) -> None:
        self.width = width
        self.height = height
        self.grid_values = [[' ' for w in range(width)] for h in range(height)]

        self.snake = Snake()
        self.apple = Apple()
        self.apple.new_position(limits=(self.width-1,self.height-1),
                                        exclude= [self.snake.get_head_position()])
        
        self._update_values()


    def pretty_print(self,) -> str:
        """
            Tool to return a str view of the grid.
        """
        _sep = '+' + '---+'*self.width + '\n'
        pretty = _sep

        for row in self.grid_values:
            _row = '|'
            for cell in row:
                _row += f' {cell} |'
            pretty += _row + '\n' + _sep

        return pretty

    def snake_move(self, move:str):
        self.snake.move(move)
        self._update_values()


    def _update_values(self) -> None:
        # reset
        self.grid_values = [[' ' for w in range(self.width)] for h in range(self.height)]

        # add apple
        _h,_w = self.apple.get_position()
        self.grid_values[_h][_w] = self.apple.MARKER

        # add snake
        for _h,_w in self.snake.get_all_positions():
            self.grid_values[_h][_w] = self.snake.MARKER

    def snake_eat_apple(self) -> bool:
        return self.snake.get_head_position() == self.apple.get_position()
    
    def snake_is_out(self) -> bool:
        _h = self.snake.get_head_position()
        return (_h[0] < 0) or (_h[1] < 0) or (_h[0] > self.height-1) or (_h[1] > self.width-1)

