# -*- coding: utf-8 -*-

"""Games GCD."""

from brain_games.engine import generate_random_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    """Return greatest common divisor of number1 and number2.

    Args:
        number1 (int): first number.
        number2 (int): second number.

    Returns:
        (str): greatest common divisor of number1 and number2.
    """
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number1 = generate_random_number()
    question_number2 = generate_random_number()
    return (
        '{0} {1}'.format(question_number1, question_number2),
        gcd(question_number1, question_number2),
    )
