# -*- coding: utf-8 -*-

import prompt


def run():
    """Запрашивает имя пользователя и выводит строку приветсвия."""
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
