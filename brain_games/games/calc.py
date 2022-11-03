from random import randint, choice


START_RANGE = 1
END_RANGE = 50
TASK = 'What is the result of the expression?'


def get_round_data():
    first_num = randint(START_RANGE, END_RANGE)
    second_num = randint(START_RANGE, END_RANGE)
    operation = choice(['+', '-', '*'])
    question = f'Question: {first_num} {operation} {second_num}'

    if operation == '+':
        return question, first_num + second_num

    elif operation == '-':
        return question, first_num - second_num

    else:
        return question, first_num * second_num
