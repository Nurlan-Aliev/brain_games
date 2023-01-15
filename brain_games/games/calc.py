from random import randint, choice
from operator import add, mul, sub


START_RANGE = 1
END_RANGE = 50
TASK = 'What is the result of the expression?'


def get_round_data():
    """Generate two random number."""
    first_num = randint(START_RANGE, END_RANGE)
    second_num = randint(START_RANGE, END_RANGE)
    operator, result = calculate(first_num, second_num)
    question = f'{first_num} {operator} {second_num}'
    return question, str(result)


def calculate(num1, num2):
    """Selects an operator calculates the resultt"""
    choice_operation = choice(['+', '-', '*'])
    dict_operator = {'+': add, '-': sub, '*': mul}
    operation = dict_operator[choice_operation]
    return choice_operation, operation(num1, num2)
