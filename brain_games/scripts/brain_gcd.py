#!/usr/bin/env python3
from brain_games.game_launch import game_launch
from brain_games.games import gcd


def main():
    """Run game gcd."""
    game_launch(gcd)


if __name__ == '__main__':
    main()
