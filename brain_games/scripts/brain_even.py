from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    games()


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def games():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(0, 100)
        print(f'Question: {number} ')
        print('Your answer: ', end='')
        user_answer = input()
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        wrong = f"'{user_answer}' is wrong answer ;(."
        correct = f"Correct answer was '{correct_answer}'."
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(wrong, correct)
            print(f"Let's try again, {name}!")
            return
        i += 1
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
