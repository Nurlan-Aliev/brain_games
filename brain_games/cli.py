import prompt


def welcome_user():
    """Greeting in the game, asks for the name and greets the player."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
