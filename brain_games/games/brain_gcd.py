"""Brain Games GCD main game body."""
import brain_games.game_engine
import math

rules = 'Find the greatest common divisor of given numbers.'


def question_maker():
    """Get GCD game question.

    Returns:
        [str, str]: question string, right answer
    """
    first_number = brain_games.game_engine.number_generator()
    second_number = brain_games.game_engine.number_generator()

    question = f'Question: {first_number} {second_number}'
    answer = gcd_solution(first_number, second_number)

    return (question, answer)


def gcd_solution(x, y):
    """Get correct answer for gcd question.

    Args:
        x (int): first operand
        y (int): second operand

    Returns:
        (str): gcd of two numbers
    """
    return str(math.gcd(x, y))
