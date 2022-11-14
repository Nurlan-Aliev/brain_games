from random import randint

START_RANGE = 1
END_RANGE = 50
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data():
    number = randint(START_RANGE, END_RANGE)

    if is_even(number):
        return number, 'yes'
    return number, 'no'


def is_even(number):
    return number % 2 == 0
