from brain_games.game_launch import game_launch
from brain_games.games.progression import progression, CONDITIONS


def main():
    game_launch(CONDITIONS, progression)


if __name__ == '__main__':
    main()
