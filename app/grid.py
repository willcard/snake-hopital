from components import Snake, Apple

class Grid:
    def __init__(self, height:int =10, width:int =10) -> None:
        self.height = height
        self.width = width
        self.grid_values = [[' ' for w in range(width)] for h in range(height)]

        self.snake = Snake()
        self.apple = Apple(limits=(self.height-1,self.width-1))
        self.apple.new_position(exclude= [self.snake.get_head_position()])
        
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

    def snake_move(self, move:str) -> bool:
        """
            Apply changes and do checkups. 
            Return game status.
        """
        self.snake.move(move)
        if self.snake_is_out() or self.snake_eat_himself():
            return False

        if self.snake_eat_apple():
            self.snake.grow_up()
            self.apple.new_position(exclude=self.snake.get_all_positions())
        self._update_values()
        return True

    def _update_values(self) -> None:
        """
            Update 2D array values based on components positions.
        """
        # reset
        self.grid_values = [[' ' for w in range(self.width)] for h in range(self.height)]

        # add apple
        _h,_w = self.apple.get_position()
        self.grid_values[_h][_w] = self.apple.MARKER

        # add snake
        for _h,_w in self.snake.get_all_positions():
            self.grid_values[_h][_w] = self.snake.MARKER

    def snake_eat_apple(self) -> bool:
        """
            Check if snake's head is on apple.
        """
        return self.snake.get_head_position() == self.apple.get_position()
    
    def snake_is_out(self) -> bool:
        """
            Check if snake's head is out of the grid.
        """
        _h = self.snake.get_head_position()
        return (_h[0] < 0) or (_h[1] < 0) or (_h[0] > self.height-1) or (_h[1] > self.width-1)
    
    def snake_eat_himself(self) -> bool:
        """
            Check if snake's head touch snake's body.
        """
        _h = self.snake.get_head_position()
        _body = self.snake.get_all_positions()[1:]
        return _h in _body

