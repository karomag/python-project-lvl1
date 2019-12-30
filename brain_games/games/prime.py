# -*- coding: utf-8 -*-

"""Games Prime."""

from brain_games.engine import generate_random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check the number is prime.

    Args:
        number (int): number for checking.

    Returns:
         (bool): True if number is prime else False.
    """
    division = 2
    while number % division != 0:
        division += 1
    if division == number:
        return True
    return False


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number = generate_random_number()
    return question_number, 'yes' if is_prime(question_number) else 'no'
