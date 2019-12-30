# -*- coding: utf-8 -*-

"""Games Calc."""

from operator import add, mul
from random import choice

from brain_games.engine import generate_random_number

DESCRIPTION = 'What is the result of the expression?'

operators = (
    ('+', add),
    ('*', mul),
)


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number1 = generate_random_number()
    question_number2 = generate_random_number()
    operator = choice(operators)
    return (
        '{0} {1} {2}'.format(question_number1, operator[0], question_number2),
        operator[1](question_number1, question_number2),
    )
