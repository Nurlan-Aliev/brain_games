import prompt


def welcome_user():
    """Asks for the name and greets the player."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
