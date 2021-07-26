"""Command line functions modul."""

import prompt


def welcome_user():
    """Enter your name > get greeting."""
    name = prompt.string('May I have your name?')
    print('{a}, {b}!'.format(a='Hello', b=name))


def get_user_answer():
    """Recive user answer.

    Returns:
        answer: prompt string
    """
    return prompt.string('Your answer: ')


def get_user_name():
    """Recive user name.

    Returns:
        username: prompt string
    """
    return prompt.string('Welcome to Brain Games!\nMay I have Your name? ')
