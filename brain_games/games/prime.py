# -*- coding: utf-8 -*-

"""Games Prime."""

from brain_games.engine import random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def correct_answer(number):
    """Return correct answer.

    Args:
        number (int): number for checking.

    Returns:
         (str): 'yes' if number is prime else 'no'
    """
    if number % 2 == 0:
        if number == 2:
            return'yes'
    division = 3
    sqr_division = division ** 2
    while sqr_division <= number and number % division != 0:
        division += 2
    if sqr_division > number:
        return 'yes'
    return 'no'


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number = random_number()
    return [question_number], correct_answer(question_number)
