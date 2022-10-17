from random import randint


START_RANGE = 2
END_RANGE = 50
CONDITIONS = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def prime():
    is_prime = randint(START_RANGE, END_RANGE)
    print(f'Question: {is_prime}')
    for index in range(START_RANGE, round(is_prime / 2) + 1):
        if is_prime % index == 0:
            correct_answer = 'no'
            return correct_answer
    correct_answer = 'yes'
    return correct_answer
