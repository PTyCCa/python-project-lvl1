"""Brain Games Calculator main body."""
import brain_games.game_engine

rules = 'What is the result of the expression?'


def question_maker():
    """Get your game question.

    Returns:
        [str, int]: qestion text, correct answer
    """
    first_number = brain_games.game_engine.number_generator()
    second_number = brain_games.game_engine.number_generator()
    operator = brain_games.game_engine.operator_generator()
    question = f'Question: {first_number} {operator} {second_number}'
    answer = calc_solution(first_number, second_number, operator)

    return (question, answer)


def calc_solution(x, y, operator):
    """Get Calc Game right answer.

    Args:
        x (int): first operand
        y (int): second operand
        operator (str): operator symbol

    Returns:
        [str]: right answer
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    return str(operations[operator](x, y))
