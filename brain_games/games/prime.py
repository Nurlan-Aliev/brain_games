from random import randint


START_RANGE = 0
END_RANGE = 50
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_data():
    number = randint(START_RANGE, END_RANGE)
    return number, is_prime(number)


def is_prime(number):
    if number == 0 or number == 1:
        return 'yes'
    for index in range(2, round(number / 2) + 1):
        if number % index == 0:
            return 'no'
    return 'yes'
