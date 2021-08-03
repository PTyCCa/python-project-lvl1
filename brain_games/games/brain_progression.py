"""Brain Games Prog main game body."""
import brain_games.game_engine
import random

rules = 'What number is missing in the progression?'


def question_maker():
    """Get your progression game question.

    Returns:
        (str, str): brain games prog question and correct answer
    """
    answer, progression = element_hider(
        brain_games.game_engine.prog_generator(),
    )
    question = 'Question: {0}'.format(progression)

    return (question, answer)


def element_hider(sequence, hider='..'):
    """Hide randome element in sequence.

    Args:
        sequence (list): random sequence
        hider (str): element hider symbol

    Returns:
        (str, str): hidden element, sequence
    """
    hidden = random.choice(sequence)
    sequence[sequence.index(hidden)] = hider

    return (str(hidden), ' '.join(sequence))
