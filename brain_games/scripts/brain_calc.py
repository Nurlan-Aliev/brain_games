from brain_games.game_launch import game_launch
from brain_games.games.calc import calc, CONDITIONS


def main():
    game_launch(CONDITIONS, calc)


if __name__ == "__main__":
    main()
