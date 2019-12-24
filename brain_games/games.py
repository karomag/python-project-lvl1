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


def run_game_even():
    """Запуск игры brain-even."""
    str_rules = 'Answer "yes" if number even otherwise answer "no".'
    user_name = cli.run(str_rules)
    for _ in range(3):
        question_number = random_question_number()
        cli.ask_question(question_number)
        user_answer = cli.get_user_answer()
        correct_answer = is_even(question_number)
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer;(. Correct answer was '{1}'.".
                format(user_answer, correct_answer),
            )
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
