from random import randint


START_RANGE = 1
END_RANGE = 50
CONDITIONS = 'Find the greatest common divisor of given numbers.'


def gcd():
    first_number = randint(START_RANGE, END_RANGE)
    second_number = randint(START_RANGE, END_RANGE)
    print(f'Question: {first_number} {second_number} ')
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
        correct_answer = first_number + second_number
    return correct_answer
