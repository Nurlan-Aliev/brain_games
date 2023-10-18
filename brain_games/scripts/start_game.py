#!/usr/bin/env python3
import inquirer

from brain_games.game_launch import game_launch
from brain_games.games import calc
from brain_games.games import prime
from brain_games.games import progression
from brain_games.games import gcd
from brain_games.games import even


def main():
    choices = [inquirer.List('choices', message='Choose one of the brain games:',
                             choices=['calc', 'prime', 'progression', 'gcd', 'even'])]
    answer = inquirer.prompt(choices)

    games = {
        'calc': calc,
        'prime': prime,
        'progression': progression,
        'gcd': gcd,
        'even': even
    }
    play_game = games[answer['choices']]

    game_launch(play_game)


if __name__ == '__main__':
    main()
