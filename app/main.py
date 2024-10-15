from grid import Grid

def main():
    grid = Grid(5,5)
    print(grid.pretty_print())

    grid.snake.move('UP')
    print(grid.snake_is_out())


if __name__ == "__main__":
    main()