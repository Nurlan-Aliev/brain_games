from random import randint

START_RANGE = 1
END_RANGE = 50
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data(lan):
    number = randint(START_RANGE, END_RANGE)
    question = f'{lan}: {number}'

    if is_even(number):
        return question, 'yes'
    return question, 'no'


def is_even(number):
    return number % 2 == 0
