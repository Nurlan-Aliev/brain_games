from random import randint


START_RANGE = 1
END_RANGE = 10
MIN_LENGTH = 6
MAX_LENGTH = 10
LOST_CHAR_FROM = 4
LOST_CHAR_TO = -5
TASK = 'What number is missing in the progression?'


def make_progression(start, end, step, lost):
    numbers = []

    while start < end:
        numbers.append(str(start))
        start += step

    lost_char = numbers[lost]
    numbers[lost] = '..'
    string_of_number = ' '.join(numbers)
    return string_of_number, lost_char


def get_round_data():
    start = randint(START_RANGE, END_RANGE)
    end = randint(MIN_LENGTH, MAX_LENGTH)
    step = randint(START_RANGE, END_RANGE)
    length = start + end * step
    lost = randint(LOST_CHAR_TO, LOST_CHAR_FROM)
    str_of_num, correct_answer = make_progression(start, length, step, lost)
    return str_of_num, correct_answer
