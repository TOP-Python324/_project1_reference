"""
Точка входа — основной управляющий код.
"""

# импорты модулей проекта
import data
import help
import game
import player
import utils


def start():
    """Инициализация приложения."""
    utils.read_players(data.players_path, data.players_db)
    utils.read_saves(data.saves_path, data.saves_db)
    
    if data.players_db:
        ...
        # help.show_commands()
    else:
        ...
        # help.show_full()
    
    player.get_player(True)


def main_menu():
    """Суперцикл главного меню."""
    while True:
        command = input(data.MESSAGES['ввод команды'])
        
        if command in data.COMMANDS['начать новую партию']:
            ...
        
        # elif command in data.COMMANDS['']:
        
        elif command in data.COMMANDS['выйти']:
            break


def end():
    """Завершение работы приложения"""
    


if __name__ == '__main__':
    start()
    main_menu()
    end()
