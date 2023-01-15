from random import randint


START_RANGE = 0
END_RANGE = 50
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_data():
    """Generate return random number and yes if number is prime otherwise no."""
    number = randint(START_RANGE, END_RANGE)
    if is_prime(number):
        return number, 'yes'
    return number, 'no'


def is_prime(number):
    """Return True if number is prime."""
    if number == 0 or number == 1:
        return False
    for index in range(2, round(number / 2) + 1):
        if number % index == 0:
            return False
    return True
