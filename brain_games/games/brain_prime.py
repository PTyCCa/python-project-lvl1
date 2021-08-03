"""Brain Games Prime main game body."""
import brain_games.game_engine
import math

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_maker():
    """Get your Prime game question.

    Returns:
        (str, str): Prime game question, correct answer
    """
    number = brain_games.game_engine.number_generator()

    question = 'Question: {0}'.format(number)
    answer = is_prime(number)

    return (question, answer)


def is_prime(number):
    """Found wether number is prime.

    Args:
        number (int): random integer

    Returns:
        (str): 'yes' or 'no' answer
    """
    if number == 2:
        return 'yes'
    if number % 2 == 0 or number <= 1:
        return 'no'

    sqrt = int((math.sqrt(number) + 1))

    for i in range(3, sqrt, 2):
        if number % i == 0:
            return 'no'

    return 'yes'
