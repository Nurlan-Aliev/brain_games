from random import randint
import math

START_RANGE = 1
END_RANGE = 50
TASK = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    first_number = randint(START_RANGE, END_RANGE)
    second_number = randint(START_RANGE, END_RANGE)
    question = f'{first_number} {second_number} '
    correct_answer = str(math.gcd(first_number, second_number))
    return question, correct_answer
