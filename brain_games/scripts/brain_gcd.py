from random import randint
import prompt


def main():
    welcome_user()
    games_gcd()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def games_gcd():
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        first = randint(1, 10)
        second = randint(1, 10)
        print(f'Question: {first} {second} ')
        print('Your answer: ', end='')
        user_answer = input()
        while first != 0 and second != 0:
            if first > second:
                first = first % second
            else:
                second = second % first
            correct_answer = first + second
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
