from random import randint

START_RANGE = 1
END_RANGE = 50
CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = randint(START_RANGE, END_RANGE)
    print(f'Question: {number} ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return correct_answer
