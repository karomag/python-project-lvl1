# -*- coding: utf-8 -*-

"""Games Even."""

from brain_games import cli
from brain_games.secfunc import random_number


def is_even(number):
    """Проверяет число на четность.

    Args:
         number: число на проверку

    Returns:
        'yes' if number is even, else 'no'
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def run():
    """Запуск игры brain-even."""
    settings = {
        'rules': 'Answer "yes" if number even otherwise answer "no".',
        'user': '',
    }
    cli.run(settings)
    user_name = settings.get('user', '')
    for _ in range(3):
        question_number = random_number()
        cli.print_question(question_number)
        user_answer = cli.get_user_answer()
        answer = is_even(question_number)
        if cli.check_answer_mistake(user_name, user_answer, answer):
            break
    else:
        cli.print_congratulations(user_name)
