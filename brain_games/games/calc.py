from random import randint, choice
from operator import add, mul, sub


START_RANGE = 1
END_RANGE = 50
TASK = 'What is the result of the expression?'


def get_round_data(lan):
    first_num = randint(START_RANGE, END_RANGE)
    second_num = randint(START_RANGE, END_RANGE)
    choice_operation = choice(['+', '-', '*'])
    dict_operator = {'+': add, '-': sub, '*': mul}
    operation = dict_operator[choice_operation]
    question = f'{lan}: {first_num} {choice_operation} {second_num}'
    return question, kalkulyator(first_num, second_num, operation)


def kalkulyator(num1, num2, operator):
    return operator(num1, num2)
