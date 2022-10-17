from brain_games.game_launch import game_launch
from brain_games.games.even import even, CONDITIONS


def main():
    game_launch(CONDITIONS, even)


if __name__ == "__main__":
    main()
