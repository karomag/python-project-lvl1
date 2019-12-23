# -*- coding: utf-8 -*-

"""Brain games main script."""

from brain_games.cli import run


def greeting():
    """Вывод приветсвия при запуске игры."""
    print('Welcome to the Brain Games!\n')


def main():
    """Основная функция модуля."""
    greeting()
    run()


if __name__ == '__main__':
    main()
