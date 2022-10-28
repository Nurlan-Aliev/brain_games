from random import randint, choice


START_RANGE = 1
END_RANGE = 50
TASK = 'What is the result of the expression?'


def get_round_data():
    first_num = randint(START_RANGE, END_RANGE)
    second_num = randint(START_RANGE, END_RANGE)
    task = choice(['+', '-', '*'])
    question = f'Question: {first_num} {task} {second_num}'
    if task == '+':
        return question, first_num + second_num
    if task == '-':
        return question, first_num - second_num
    if task == '*':
        return question, first_num * second_num
