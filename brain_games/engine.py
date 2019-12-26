# -*- coding: utf-8 -*-

"""Module with a game engine. Startup function exported run(game)."""

from random import SystemRandom

from brain_games.cli import get_user_answer, get_user_name

ROUNDS = 3


def random_number(start=0, end=100):
    """Return random number using sources provided by the operating system.

    Args:
        start (int): start position to generate (default=0)
        end (int): end position to generate (default=100)

    Returns:
        Return random integer in range [start, end], including both end points.
    """
    crypto = SystemRandom()
    return crypto.randint(start, end)


def random_operate(seq):
    """Return random element using sources provided by the operating system.

    Args:
        seq (sequence): non-empty sequence

    Returns:
        Choose a random element from a non-empty sequence.
    """
    crypto = SystemRandom()
    return crypto.choice(seq)


def run(game=None):
    """Run game.

    Args:
        game: game from brain_games.games
    """
    if game is None:
        return

    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION, '\n')
    user_name = get_user_name()
    print('Hello, {0}!\n'.format(user_name))

    for _ in range(ROUNDS):
        question, correct_answer = game.get_game_task()
        print('Question:', *question)
        user_answer = get_user_answer()
        if correct_answer == user_answer:
            print('Correct!')
            continue

            template = '{0} is wrong answer;(. Correct answer was {1}.'
            print(template.format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
