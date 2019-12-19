#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from brain_games.cli import run


def greeting():
    """Выводит строку приветствия при запуске приложения."""
    print('Welcome to the Brain Games!\n')


def main():
    """Основная функция модуля."""
    greeting()
    run()


if __name__ == '__main__':
    main()
