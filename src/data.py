"""
Глобальные переменные и условные константы.
"""

# импорты модулей стандартной библиотеки
from pathlib import Path
from sys import argv, path


ROOT_DIR = Path(path[0]).parent

test_path = 'test/' if 'test' in argv else ''
players_path = ROOT_DIR / f'data/{test_path}players.ini'
saves_path = ROOT_DIR / f'data/{test_path}saves.txt'


players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], tuple[int, list[int]]] = {}

