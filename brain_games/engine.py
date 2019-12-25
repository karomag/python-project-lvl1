# -*- coding: utf-8 -*-

"""Module with a game engine. Startup function exported run()."""

from random import SystemRandom


def gen_random_number(start=0, end=100):
    """Return random number using sources provided by the operating system.

    Args:
        start (int): start position to generate (default=0)
        end (int): end position to generate (default=100)

    Returns:
        Return random integer in range [start, end], including both end points.
    """
    crypto = SystemRandom()
    return crypto.randint(start, end)


def gen_random_operate(seq):
    """Return random element using sources provided by the operating system.

    Args:
        seq (sequence): non-empty sequence

    Returns:
        Choose a random element from a non-empty sequence.
    """
    crypto = SystemRandom()
    return crypto.choice(seq)
