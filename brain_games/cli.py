"""Приветствие."""

import prompt


def welcome_user():
    """Enter your name > get greeting."""
    name = prompt.string('May I have your name?')
    print('{a}, {b}!'.format(a='Hello', b=name))
