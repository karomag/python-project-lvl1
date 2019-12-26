# -*- coding: utf-8 -*-

"""Games Progression."""

from brain_games.engine import random_number

DESCRIPTION = 'What number is missing in the progression?'
LEN_PROGRESSION = 10


def correct_answer(progression, index_hidden_element):
    """Return correct answer.

    Args:
        progression (list): Arithmetic progression.
        index_hidden_element (int): index member of progression.

    Returns:
        (str): hidden member arithmetic progression.
    """
    return progression[index_hidden_element]


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    step_progression = random_number(1, 10)
    index_hidden_element = random_number(0, LEN_PROGRESSION - 1)
    progression = []
    for step in range(1, LEN_PROGRESSION + 1):
        progression.append(str(1 + (step - 1) * step_progression))

    task_progression = progression[:]
    task_progression.pop(index_hidden_element)
    task_progression.insert(index_hidden_element, '...')
    return task_progression, correct_answer(progression, index_hidden_element)
