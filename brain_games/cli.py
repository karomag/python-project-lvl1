# -*- coding: utf-8 -*-

"""Command line tools."""

import prompt


def run(str_rules):
    """Запрашивает имя пользователя и возвращает строку приветсвия.

    Args:
        str_rules: string with game rules

    Returns:
        user_name - имя введенное пользователем
    """
    print('Welcome to the Brain Games!')
    print()
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(user_name))
    return user_name


def get_user_answer():
    """Запрашивает у пользователя ответ на вопрос.

    Returns:
        answer - ответ введенный пользователем
    """
    return prompt.string('Your answer: ')


def ask_question(task):
    """Выводит в консоль вопрос с заданием для пользователя.

    Args:
        task: task for user

    Returns:
        answer - user's answer
    """
    return print('Question:', task)
