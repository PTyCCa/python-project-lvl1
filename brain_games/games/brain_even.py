"""Brain Games Even main body."""
import brain_games.game_engine

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_maker():
    """Get your Even game question.

    Returns:
        [str, int]: question string, right answer
    """
    number = brain_games.game_engine.number_generator()
    question = 'Question: {0}'.format(number)
    answer = is_even_answer(number)

    return (question, answer)


def is_even_answer(number):
    """Int even or not checker.

    Args:
        number (int): game questioned int

    Returns:
        [str]: correct answer
    """
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
