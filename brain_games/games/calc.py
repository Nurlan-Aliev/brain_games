from random import randint


START_RANGE = 1
END_RANGE = 50
CONDITIONS = 'What is the result of the expression?'


def calc():
    first_num = randint(1, 50)
    second_num = randint(1, 50)
    plus = first_num + second_num
    minus = first_num - second_num
    multiplication = first_num * second_num
    task = [plus, minus, multiplication]
    question = task[randint(0, 2)]
    if question == plus:
        print(f'Question: {first_num} + {second_num}')
    if question == minus:
        print(f'Question: {first_num} - {second_num}')
    if question == multiplication:
        print(f'Question: {first_num} * {second_num}')
    return question
