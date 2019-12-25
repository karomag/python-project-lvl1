# -*- coding: utf-8 -*-

"""Games Calc."""

from operator import add, mul

from brain_games.engine import random_number, random_operate

DESCRIPTION = 'What is the result of the expression?'

operators = [
    {'name': '+', 'func': add},
    {'name': '*', 'func': mul},
]


def correct_answer(number1, number2, operator):
    """Return correct answer.

    Args:
        number1 (int): first number.
        number2 (int): second number.
        operator: function for numbers.

    Returns:
        (str): result operator(number1, number2).
    """
    return str(operator(number1, number2))


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    question_number1 = random_number()
    question_number2 = random_number()
    operator = random_operate(operators)
    return (
        [question_number1, operator['name'], question_number2],
        correct_answer(question_number1, question_number2, operator['func']),
    )
