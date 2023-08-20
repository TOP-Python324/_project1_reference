"""
Глобальные переменные и условные константы.
"""

# импорты модулей стандартной библиотеки
from pathlib import Path
from re import Pattern, compile
from sys import argv, path
from typing import Callable


ROOT_DIR = Path(path[0]).parent

test_path = 'test/' if 'test' in argv else ''
players_path = ROOT_DIR / f'data/{test_path}players.ini'
saves_path = ROOT_DIR / f'data/{test_path}saves.txt'


players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], tuple[int, list[int]]] = {}


pat_player_name: Pattern = compile(r'[A-Za-zА-Яа-я]\w*')


authorized: str = None

active_players_names: list[str] = []
active_players_funcs: list[Callable] = []


MESSAGES = {
    'ввод имени': "\n введите имя пользователя > ",
    'некорректное имя': " _ имя пользователя должно начинаться с буквы и далее содержать только буквы, цифры и символ '_' _",
    # '': "",
}

