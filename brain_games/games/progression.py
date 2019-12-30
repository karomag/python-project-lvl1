# -*- coding: utf-8 -*-

"""Games Progression."""

from brain_games.engine import generate_random_number

DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def get_game_task():
    """Return parameters for task.

    Returns:
        (tuple): (question, correct_answer).
    """
    step_progression = generate_random_number(1, 10)
    hidden_element_index = generate_random_number(0, LENGTH_PROGRESSION - 1)
    progression = []
    for step in range(1, LENGTH_PROGRESSION + 1):
        progression.append(str(1 + (step - 1) * step_progression))
    task_progression = progression[:]
    task_progression[hidden_element_index] = '...'
    return ' '.join(task_progression), progression[hidden_element_index]
