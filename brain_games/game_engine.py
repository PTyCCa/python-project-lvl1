"""Game common functions modul."""
import random

import brain_games.cli


def welcome_user():
    """Greets User.

    Returns:
        user_name: string {Hello}, {user_name}! format
    """
    user_name = brain_games.cli.get_user_name()
    print('{a}, {b}!'.format(a='Hello', b=user_name))

    return user_name


def number_generator():
    """Make random int.

    Returns:
        int: randome int in range 0 to 1000
    """
    return random.randint(0, 1000)


def answer_checker(correct_answer, user_answer):
    """Insert answer and get weather it right.

    Args:
        correct_answer (str): quiz correct answer
        user_answer (str): user answer

    Returns:
        bool, string: True or False, string variant
    """
    if user_answer == correct_answer:
        message = 'Correct!'
        return (True, message)

    message = "'{wr}' is wrong answer ;(. Correct answer was '{cr}'."
    return (False, message.format(wr=user_answer, cr=correct_answer))


def run(game=None):
    """Run desired game.

    Args:
        game (str, optional): Name of Brain Game. Defaults to None.
    """
    if game:
        user_name = welcome_user()
        print(game.rules)
        engine(user_name, game.question_maker)


def engine(user_name, play):
    """Brain Games common body.

    Args:
        user_name (str): recived user name
        play (str): Brain Games game name
    """
    attepts = 3
    while attepts > 0:
        question, correct_answer = play()
        print(question)
        result, message = answer_checker(
            correct_answer, brain_games.cli.get_user_answer(),
        )
        print(message)

        if not result:
            print("Let's try again, {0}!".format(user_name))
            return
        attepts -= 1
    print('Congratulations, {0}!'.format(user_name))


def operator_generator():
    """Get random operator.

    Returns:
        [str]: random operator from dictionary
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    return random.choice(list(operations.keys()))
