# -*- coding: utf-8 -*-

"""Module with a game engine. Startup function exported run(game)."""

from random import randint

from brain_games.cli import get_user_answer, get_user_name

ROUNDS = 3


def generate_random_number(start=0, end=100):
    """Return random number x start <= x <= end.

    Args:
        start (int): start position to generate (default=0)
        end (int): end position to generate (default=100)

    Returns:
        Return random integer in range [start, end], including both end points.
    """
    return randint(start, end)


def welcome(description):
    """Print welcome message.

    Args:
        description: game description
    """
    print('Welcome to the Brain Games!')
    print(description)
    print()


def run(game=None):
    """Run game.

    Args:
        game: game from brain_games.games
    """
    if game is None:
        return
    welcome(game.DESCRIPTION)
    user_name = get_user_name()
    print('Hello, {0}!'.format(user_name))
    print()
    for _ in range(ROUNDS):
        question, correct_answer = game.get_game_task()
        print('Question:', question)
        user_answer = get_user_answer()
        if str(correct_answer) != user_answer:
            template = "'{0}' is wrong answer;(. Correct answer was '{1}'."
            print(template.format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(user_name))
