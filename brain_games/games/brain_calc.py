# -*- coding: utf-8 -*-

"""Games Calc."""

from brain_games import cli
from brain_games.secfunc import random_number, random_operate


def correct_answer(number1, number2, operate):
    """Проверяет число на четность.

    Args:
        number1: первое число
        number2: второе число
        operate: операция

    Returns:
        'yes' if number is even, else 'no'
    """
    if operate == '+':
        return number1 + number2
    elif operate == '*':
        return number1 * number2


def run():
    """Запуск игры brain-even."""
    settings = {
        'rules': 'What is the result of the expression?',
        'user': '',
    }
    cli.run(settings)

    for _ in range(3):
        question_number1 = random_number()
        question_number2 = random_number()
        operate = random_operate()
        cli.print_question([question_number1, operate, question_number2])

        mistake = cli.check_answer_mistake(
            settings['user'],
            int(cli.get_user_answer()),
            correct_answer(question_number1, question_number2, operate),
        )
        if mistake:
            break
    else:
        cli.print_congratulations(settings['user'])
