# -*- coding: utf-8 -*-

"""Games Even."""

from brain_games.engine import generate_random_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """Check the number is even.

    Args:
        number (int): number.

    Returns:
        (bool): True if number is even else False.
    """
    return number % 2 == 0


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number = generate_random_number()
    return question_number, 'yes' if is_even(question_number) else 'no'
