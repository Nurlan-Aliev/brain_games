from random import randint
import prompt


def main():
    welcome_user()
    games_calc()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def games_calc():
    print('What is the result of the expression?')
    for i in range(3):
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        plus = num1 + num2
        minus = num1 - num2
        multiplication = num1 * num2
        task = [plus, minus, multiplication]
        question = task[randint(0, 2)]
        if question == plus:
            print(f'Question: {num1} + {num2}')
        if question == minus:
            print(f'Question: {num1} - {num2}')
        if question == multiplication:
            print(f'Question: {num1} * {num2}')
        print('Your answer: ', end='')
        user_answer = int(input())
        wrong = f"'{user_answer}' is wrong answer ;(."
        correct = f"Correct answer was '{question}'."
        if question == user_answer:
            print('Correct!')
        else:
            print(wrong, correct)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
