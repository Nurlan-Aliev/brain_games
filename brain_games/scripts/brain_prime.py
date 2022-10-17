from brain_games.game_launch import game_launch
from brain_games.games.prime import prime, CONDITIONS


def main():
    game_launch(CONDITIONS, prime)


if __name__ == '__main__':
    main()
