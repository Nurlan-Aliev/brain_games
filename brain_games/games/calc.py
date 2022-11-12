from random import randint, choice
from operator import add, mul, sub


START_RANGE = 1
END_RANGE = 50
TASK = 'What is the result of the expression?'


def get_round_data():
    first_num = randint(START_RANGE, END_RANGE)
    second_num = randint(START_RANGE, END_RANGE)
    choice_operation = choice(['+', '-', '*'])
    question = f'{first_num} {choice_operation} {second_num}'
    return question, str(calculate(first_num, second_num, choice_operation))


def calculate(num1, num2, operator):
    dict_operator = {'+': add, '-': sub, '*': mul}
    operation = dict_operator[operator]
    return operation(num1, num2)
