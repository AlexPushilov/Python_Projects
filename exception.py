import os
from sys import exit


def try_change_dir(way):
    """Эта фунция предназначена для проверки правильности пути, введеного пользователем"""

    try:
        os.chdir(way)
    except FileNotFoundError:
        print("Упс! Ошибка!")
        print("Вы ввели несуществующий путь к директории!")
        print()
        os.system("pause")
        exit()
    except WindowsError:
        print("Упс! Ошибка!")
        print("Наверное вы сразу же нажали клавишу Enter")
        print()
        os.system("pause")
        exit()
