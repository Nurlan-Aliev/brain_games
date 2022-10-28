from random import randint


START_RANGE = 1
END_RANGE = 10
MIN_LENGTH = 6
MAX_LENGTH = 10
LOST_CHAR_FROM = 4
LOST_CHAR_TO = -5
TASK = 'What number is missing in the progression?'


def get_round_data():
    number_of_start = randint(START_RANGE, END_RANGE)
    len_progression = randint(MIN_LENGTH, MAX_LENGTH)
    step_progression = randint(START_RANGE, END_RANGE)
    len_progression = number_of_start + len_progression * step_progression
    list_of_number = []
    while number_of_start < len_progression:
        list_of_number.append(number_of_start)
        number_of_start += step_progression
    string_of_number = ''
    lost_char = randint(LOST_CHAR_TO, LOST_CHAR_FROM)
    correct_answer = list_of_number[lost_char]
    list_of_number[lost_char] = '..'
    for char in list_of_number:
        string_of_number += str(char) + ' '
    string_of_number = string_of_number.strip()
    question = f'Question: {string_of_number} '
    return question, correct_answer
