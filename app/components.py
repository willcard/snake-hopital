import random

class Apple:
    MARKER = 'O'
    def __init__(self, limits:tuple[int,int]) -> None:
        self.position = (1,1)
        self.limits = limits

    def new_position(self, exclude=list[tuple[int,int]]) -> None:
        """
            Smart randomly change apple's position.
        """
        isok = False
        while not isok:
            _h = random.randint(0,self.limits[0])
            _w = random.randint(0,self.limits[1])
            if not (((_h,_w) in exclude) or ((_h,_w) == self.position)):
                isok = True
        self.position = (_h,_w)

    def get_position(self) -> tuple[int,int]:
        """
            Return apple's position.
        """
        return self.position
    


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
        """
            Return snake's head position.
        """
        return self.head_position
    
    def get_all_positions(self) -> list[tuple[int,int]]:
        """
            Return snake's body positions.
        """
        return self.all_positions
    
    def get_length(self) -> int:
        """
            Return snake's length.
        """
        return self.length
    
    def grow_up(self) -> None:
        """
            Make snake grow up.
        """ 
        self.all_positions.append(self.previous_tail_position)
        self.length += 1
    
    def _move_up(self) -> tuple[int,int]:
        """
            Return new head's position, for up move.
        """
        _head = self.head_position
        return _head[0]-1,_head[1]
    
    def _move_down(self) -> tuple[int,int]:
        """
            Return new head's position, for down move.
        """
        _head = self.head_position
        return _head[0]+1,_head[1]
    
    def _move_left(self) -> tuple[int,int]:
        """
            Return new head's position, for left move.
        """
        _head = self.head_position
        return _head[0],_head[1]-1
    
    def _move_right(self) -> tuple[int,int]:
        """
            Return new head's position, for right move.
        """
        _head = self.head_position
        return _head[0],_head[1]+1

    def move(self, direction:str) -> None:
        """
            Update positions based on passed move.
        """
        assert direction in self.ALLOWED_DIRECTIONS

        if direction == 'UP':
            _head = self._move_up()
        elif direction == 'DOWN':
            _head = self._move_down()
        elif direction == 'LEFT':
            _head = self._move_left()
        else:
            _head = self._move_right()

        self.head_position = _head
        self.all_positions.insert(0,_head)
        self.previous_tail_position = self.all_positions[-1]
        self.all_positions = self.all_positions[:-1]
