# -*- coding: utf-8 -*-

"""Games."""

from random import SystemRandom

from brain_games import cli


def random_question_number():
    """Возвращает случайное целое число из диапозона.

    Returns:
        int[min_number, max_number]
    """
    min_number = 1
    max_number = 100
    crypto = SystemRandom()
    return crypto.randint(min_number, max_number)


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
        question_number = random_question_number()
        cli.print_question(question_number)
        user_answer = cli.get_user_answer()
        correct_answer = is_even(question_number)
        if cli.check_answer_mistake(user_name, user_answer, correct_answer):
            break
    else:
        cli.print_congratulations(user_name)
