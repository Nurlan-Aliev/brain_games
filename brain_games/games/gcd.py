from random import randint
import math

START_RANGE = 1
END_RANGE = 50
TASK = 'Find the greatest common divisor of given numbers.'


def get_round_data(lan):
    first_number = randint(START_RANGE, END_RANGE)
    second_number = randint(START_RANGE, END_RANGE)
    question = f'{lan}: {first_number} {second_number} '
    correct_answer = math.gcd(first_number, second_number)
    return question, correct_answer
