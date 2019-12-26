# -*- coding: utf-8 -*-

"""Games GCD."""

from math import gcd

from brain_games.engine import random_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def correct_answer(number1, number2):
    """Return correct answer.

    Args:
        number1 (int): first number.
        number2 (int): second number.

    Returns:
        (str): greatest common divisor of number1 and number2.
    """
    return str(gcd(number1, number2))


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number1 = random_number()
    question_number2 = random_number()
    return (
        [question_number1, question_number2],
        correct_answer(question_number1, question_number2),
    )
