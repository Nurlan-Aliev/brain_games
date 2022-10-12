from random import randint
from prompt import string


def main():
    welcome_user()
    brain_progression()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = string('May I have your name? ')
    print(f'Hello, {name}!')


def brain_progression():
    print('What number is missing in the progression?')
    for i in range(3):
        first = randint(1, 10)
        second = randint(5, 10)
        step = randint(1, 10)
        second = second * step + first
        list_of_number = []
        while first < second:
            list_of_number.append(first)
            first += step
        string_of_number = ''
        lost_char = randint(-5, 4)
        correct_answer = list_of_number[lost_char]
        list_of_number[lost_char] = '..'
        for char in list_of_number:
            string_of_number += str(char) + ' '
        son = string_of_number.strip()
        print(f'Question: {son} ')
        print('Your answer: ', end='')
        user_answer = input()
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
