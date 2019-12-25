# -*- coding: utf-8 -*-

"""Command line tools."""

import prompt


def get_user_answer():
    """Ask user's answer.

    Returns:
        (str): User's answer.
    """
    return prompt.string('Your answer: ')


def get_user_name():
    """Ask user's name.

    Returns:
        (str): User's name.
    """
    return prompt.string('May I have your name? ')
