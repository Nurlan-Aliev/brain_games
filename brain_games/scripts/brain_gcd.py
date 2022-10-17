from brain_games.game_launch import game_launch
from brain_games.games.gcd import gcd, CONDITIONS


def main():
    game_launch(CONDITIONS, gcd)


if __name__ == '__main__':
    main()
