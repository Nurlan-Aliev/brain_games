from random import randint


START_RANGE = 2
END_RANGE = 50
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_data():
    number = randint(START_RANGE, END_RANGE)
    question = f'{number}'
    return question, is_prime(number, START_RANGE)


def is_prime(number, start):
    for index in range(start, round(number / 2) + 1):
        if number % index == 0:
            return 'no'
    return 'yes'
