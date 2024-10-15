import random

class Grid:
    def __init__(self, width:int =10, height:int =10) -> None:
        self.width = width
        self.height = height
        self.grid_values = [[' ' for w in range(width)] for h in range(height)]

        self.snake = Snake()
        self.update_snake()

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
            self.grid_values[_h][_w] = self.apple.MARKER
        else:
            #TODO
            pass

    def update_snake(self) -> None:
        for _h,_w in self.snake.get_all_positions():
            self.grid_values[_h][_w] = self.snake.MARKER

    def snake_eat_apple(self) -> bool:
        return self.snake.get_head_position() == self.apple.get_position()
    
    def snake_is_out(self) -> bool:
        _h = self.snake.get_head_position()
        return (_h[0] < 0) or (_h[1] < 0) or (_h[0] > self.height-1) or (_h[1] > self.width-1)




class Snake:
    ALLOWED_DIRECTIONS = ('UP','DOWN','LEFT','RIGHT')
    MARKER = '#'
    def __init__(self) -> None:
        self.length = 1
        self.direction = 'DOWN'
        self.head_position = (0,0)
        self.previous_tail_position = self.head_position
        self.all_positions = [self.head_position]

    def get_head_position(self) -> tuple[int,int]:
        return self.head_position
    
    def get_all_positions(self) -> tuple[int,int]:
        return self.all_positions
    
    def get_length(self) -> int:
        return self.length
    
    def grow_up(self) -> None: 
        self.all_positions.append(self.previous_tail_position)
        self.length += 1
    
    def move_up(self) -> tuple[int,int]:
        _head = self.head_position
        _head[0] -= 1
        return _head
    
    def move_down(self) -> tuple[int,int]:
        _head = self.head_position
        _head[0] += 1
        return _head
    
    def move_left(self) -> tuple[int,int]:
        _head = self.head_position
        _head[1] -= 1
        return _head
    
    def move_right(self) -> tuple[int,int]:
        _head = self.head_position
        _head[1] += 1
        return _head

    def move(self, direction:str) -> None:
        if direction == 'UP':
            _head = self.move_up()
        if direction == 'DOWN':
            _head = self.move_down()
        if direction == 'LEFT':
            _head = self.move_left()
        else:
            _head = self.move_right()

        self.all_positions.insert(0,_head)
        self.previous_tail_position = self.all_positions[-1]
        self.all_positions = self.all_positions[:-1]
        


class Apple:
    MARKER = 'O'
    def __init__(self) -> None:
        self.position = (1,1)

    def new_position(self, limits:tuple[int,int], exclude=list[tuple[int,int]]) -> None:
        isok = False
        while not isok:
            _w = random.randint(0,limits[0])
            _h = random.randint(0,limits[1])
            if not (((_h,_w) in exclude) or ((_h,_w) == self.position)):
                isok = True
        self.position = (_h,_w)

    def get_position(self) -> tuple[int,int]:
        return self.position