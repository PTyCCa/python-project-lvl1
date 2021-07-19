#!/usr/bin/env python3
"""Even game modul."""

import random

import prompt


def is_even_game():
    """Even or not quiz game."""
    name = prompt.string('May I Have your name? ')
    print('{a}, {b}!'.format(a='Hello', b=name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 0
    answer_vars = {'1': 'yes', '2': 'no'}

    while attempts < 3:
        riddle_number = random.randint(0, 1000)
        if riddle_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('{a}: {b}'.format(a='Question:', b=riddle_number))

        user_answer = prompt.string('Your answer: ')

        if user_answer not in answer_vars.values():
            print('"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet\'s try again, {2}!'.format(
                user_answer, correct_answer, name),
            )
            break

        if riddle_number % 2 == 0 and user_answer == 'no' or riddle_number % 2 != 0 and user_answer == 'yes':
            print('"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet\'s try again, {2}!'.format(
                user_answer, correct_answer, name),
            )
            break
        else:
            print('Correct!')
            attempts += 1

    if attempts == 3:
        print('Congratulations, {0}!'.format(name))


def main():
    """Game start invitation."""
    is_even_game()


if __name__ == '__main__':
    main()
