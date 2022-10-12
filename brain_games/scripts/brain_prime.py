from random import randint
from prompt import string


def main():
    welcome_user()
    brain_prime()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = string('May I have your name? ')
    print(f'Hello, {name}!')


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    for i in range(3):
        number = randint(2, 100)

        def prime(finder):
            for index in range(2, round(finder / 2) + 1):
                if finder % index == 0:
                    return 'no'
            return 'yes'
        print(f'Question: {number}')
        print('Your answer: ', end='')
        user_answer = input()
        correct_answer = prime(number)
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
