# -*- coding: utf-8 -*-

"""Command line tools."""

import prompt


def run():
    """Запрашивает имя пользователя и возвращает строку приветсвия.

    Returns:
        user_name - имя введенное пользователем
    """
    return prompt.string('May I have your name? ')


def get_user_answer():
    """Запрашивает у пользователя ответ на вопрос.

    Returns:
        answer - ответ введенный пользователем
    """
    return prompt.string('Your answer: ')
