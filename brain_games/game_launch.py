from prompt import string
from brain_games.cli import welcome_user

GAME_ROUNDS = 3


def game_launch(game):
    """
    Greets the player.
    Asks for a name.
    Checks if the answer is correct.
    """
    user_name = welcome_user()
    print(game.TASK)

    for i in range(GAME_ROUNDS):
        question, correct_answer = game.get_round_data()
        print('Question:', question)
        user_answer = string('Your answer: ').lower()

        if user_answer == correct_answer:
            print('Correct')

        else:
            print(f"'{user_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
