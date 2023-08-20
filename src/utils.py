"""
Вспомогательные функции.
"""

# импорты модулей стандартной библиотеки
from configparser import ConfigParser
from pathlib import Path
from pprint import pprint
# импорты модулей проекта
import data


def read_players(filein_path: Path, buffer: dict) -> None:
    """"""
    players_data = ConfigParser()
    players_data.read(filein_path)
    buffer |= {
        player: {
            k: int(v) 
            for k, v in players_data[player].items()
        }
        for player in players_data.sections()
    }


def read_saves(filein_path: Path, buffer: dict) -> None:
    """"""
    try:
        saves_data = filein_path.read_text(encoding='utf-8').split('\n')
    except FileNotFoundError:
        pass
    else:
        for line in saves_data:
            try:
                players, dim, turns = line.split('!')
            except ValueError:
                return
            players = tuple(players.split(','))
            dim = int(dim)
            turns = [int(t) for t in turns.split(',')]
            buffer |= {players: (dim, turns)}


def write_players(buffer: dict, fileout_path: Path) -> None:
    """"""
    players_data = ConfigParser()
    players_data.read_dict(buffer)
    with open(fileout_path, 'w', encoding='utf-8') as fileout:
        players_data.write(fileout)


def write_saves(buffer: dict, fileout_path: Path) -> None:
    """"""
    players_data = []
    for players, turns in buffer.items():
        dim, turns = turns
        players = ','.join(players)
        turns = ','.join(str(t) for t in turns)
        players_data.append('!'.join((players, str(dim), turns)))
    with open(fileout_path, 'w', encoding='utf-8') as fileout:
        fileout.write('\n'.join(players_data))


def change_dim(new_dim: int) -> None:
    """"""
    data.dim = new_dim
    data.all_cells = new_dim**2
    data.dim_range = range(new_dim)
    data.all_cells_range = range(1, data.all_cells+1)
    ...
