from game import Game

TEST_MOVES = ('DOWN','DOWN','RIGHT','DOWN','RIGHT')

def main():
    game = Game()

    for move in TEST_MOVES:
        game.run(move)

if __name__ == "__main__":
    main()