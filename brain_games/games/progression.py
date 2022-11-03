from random import randint


START_RANGE = 1
END_RANGE = 10
MIN_LENGTH = 6
MAX_LENGTH = 10
LOST_CHAR_FROM = 4
LOST_CHAR_TO = -5
TASK = 'What number is missing in the progression?'


def make_progression(start, end, step):
    list_of_number = []

    while start < end:
        list_of_number.append(str(start))
        start += step

    lost = randint(LOST_CHAR_TO, LOST_CHAR_FROM)
    lost_char = list_of_number[lost]
    list_of_number[lost] = '..'
    string_of_number = ' '.join(list_of_number)
    return string_of_number, lost_char


def get_round_data():
    start = randint(START_RANGE, END_RANGE)
    len_progression = randint(MIN_LENGTH, MAX_LENGTH)
    step_progression = randint(START_RANGE, END_RANGE)
    len_progression = start + len_progression * step_progression
    result = make_progression(start, len_progression, step_progression)
    string_of_num, correct_answer = result
    question = f'Question: {string_of_num} '
    return question, correct_answer
