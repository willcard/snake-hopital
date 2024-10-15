class Grid:
    def __init__(self, width:int =10, height:int =10) -> None:
        self.width = width
        self.height = height
        self.grid_values = [[' ' for w in range(width)] for h in range(height)]

        self.apple = Apple()
        self.snake = Snake()

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
    
    def update_apple(self, width, height) -> None:
        pass


class Snake:
    DIRECTIONS = ('UP','DOWN','LEFT','RIGHT')
    def __init__(self) -> None:
        self.length = 1
        self.position = (0,0)
        self.direction = 'UP'


class Apple:
    def __init__(self) -> None:
        self.position = (2,2)