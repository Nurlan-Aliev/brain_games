from random import randint

START_RANGE = 1
END_RANGE = 50
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data():
    number = randint(START_RANGE, END_RANGE)
    question = f'Question: {number}'
    if number % 2 == 0:
        return question, 'yes'
    return question, 'no'
