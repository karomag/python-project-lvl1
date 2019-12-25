# -*- coding: utf-8 -*-

"""Games Even."""

from brain_games.engine import random_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def correct_answer(number):
    """Return correct answer.

    Args:
        number (int): number.

    Returns:
        (str): 'yes' if number is even else 'no'.
    """
    return 'yes' if number % 2 == 0 else 'no'


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number = random_number()
    return [question_number], correct_answer(question_number)
