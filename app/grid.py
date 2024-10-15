import random

class Grid:
    def __init__(self, width:int =10, height:int =10) -> None:
        self.width = width
        self.height = height
        self.grid_values = [[' ' for w in range(width)] for h in range(height)]

        self.snake = Snake()
        self.update_snake(first=True)

        self.apple = Apple()
        self.apple.new_position(limits=(self.width-1,self.height-1),
                                        exclude= [self.snake.get_head_position()])
        self.update_apple(first=True)


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
    
    def update_apple(self, first=False) -> None:
        if first:
            _w,_h = self.apple.get_position()
            self.grid_values[_w][_h] = 'O'
        else:
            #TODO
            pass

    def update_snake(self, first=False) -> None:
        if first:
            _w,_h = self.snake.get_head_position()
            self.grid_values[_w][_h] = self.snake.MARKER
        else:
            #TODO
            pass


class Snake:
    ALLOWED_DIRECTIONS = ('UP','DOWN','LEFT','RIGHT')
    MARKER = '#'
    def __init__(self) -> None:
        self.length = 1
        self.head_position = (0,0)
        self.tail_position = self.head_position
        self.direction = 'DOWN'

    def grow_up(self) -> None:
        pass

    def get_head_position(self) -> tuple[int,int]:
        return self.head_position
    

class Apple:
    MARKER = 'O'
    def __init__(self) -> None:
        self.position = (1,1)

    def new_position(self, limits:tuple[int,int], exclude=list[tuple[int,int]]) -> None:
        isok = False
        while not isok:
            _w = random.randint(0,limits[0])
            _h = random.randint(0,limits[1])
            if not (_w,_h) in exclude:
                isok = True
        self.position = (_w,_h)

    def get_position(self) -> tuple[int,int]:
        return self.position