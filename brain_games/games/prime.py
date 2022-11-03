from random import randint


START_RANGE = 2
END_RANGE = 50
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_data():
    number = randint(START_RANGE, END_RANGE)
    question = f'Question: {number}'

    for index in range(START_RANGE, round(number / 2) + 1):

        if is_prime(number, index):
            correct_answer = 'no'
            return question, correct_answer

    correct_answer = 'yes'
    return question, correct_answer


def is_prime(number, index):
    return number % index == 0