# -*- coding: utf-8 -*-

"""Command line tools."""

import prompt


def run(settings=None):
    """Запрашивает имя пользователя и возвращает строку приветсвия.

    Args:
        settings: dic{rules:str, user:str}
    """
    if settings is None:
        settings = {'rules': '', 'user': ''}

    print('Welcome to the Brain Games!')
    print(settings['rules'])
    print()
    settings['user'] = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(settings['user']))


def get_user_answer():
    """Запрашивает у пользователя ответ на вопрос.

    Returns:
        answer - ответ введенный пользователем
    """
    return prompt.string('Your answer: ')


def print_question(lst):
    """Выводит в консоль вопрос с заданием для пользователя.

    Args:
        lst: args for task for user.
    """
    print('Question:', end=' ')
    print(*lst)


def print_congratulations(user_name):
    """Выводит в консоль поздравление пользователя с победой.

    Args:
        user_name: user name
    """
    print('Congratulations, {0}!'.format(user_name))


def check_answer_mistake(user_name, user_answer, correct_answer):
    """Сравнивает ответ пользователя с правильным.

    Args:
        user_name: user name
        user_answer: user answer
        correct_answer: correct answer

    Returns:
        checking_result: result of checking
    """
    if correct_answer == user_answer:
        print('Correct!')
        return False

    print(
        "'{0}' is wrong answer;(. Correct answer was '{1}'.".
        format(user_answer, correct_answer),
    )
    print("Let's try again, {0}!".format(user_name))
    return True
