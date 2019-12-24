# -*- coding: utf-8 -*-

"""Secondary functions."""

from random import SystemRandom


def random_number():
    """Возвращает случайное целое число из диапозона.

    Returns:
        int[min_number, max_number]
    """
    min_number = 1
    max_number = 100
    crypto = SystemRandom()
    return crypto.randint(min_number, max_number)


def random_operate():
    """Возвращает случайную операцию.

    Returns:
        '+' or '*'
    """
    crypto = SystemRandom()
    return crypto.choice(['+', '*'])
