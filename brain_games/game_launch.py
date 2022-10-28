from prompt import string


GAME_ROUNDS = 3


def game_launch(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.TASK)
    for i in range(GAME_ROUNDS):
        question, correct_answer = game.get_round_data()
        print(question)
        user_answer = string('Your answer: ').lower()
        if user_answer == str(correct_answer):
            print('Correct')
        else:
            wrong = f"'{user_answer}' is wrong answer ;(."
            correct = f"Correct answer was '{correct_answer}'."
            print(wrong, correct)
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
