import os
from time import ctime
from calendar import number_of_month


def date_of_create(way):
    """Эта фунция возвращает словарь.

Он состоит из имен папок/файлов и их времени создания"""

    dict_of_files = {}
    for file in os.listdir(way):
        time_of_create = ctime(os.path.getctime(file))
        time = ".".join(time_of_create[11:19].split(":"))
        month = time_of_create[4:7]
        year = time_of_create[20:]
        day = time_of_create[8:10]
        extension = os.path.splitext(file)
        if int(day) < 10:
            day = "0" + day
        full_time_of_create = f"{day}.{number_of_month(month)}.{year}_{time}{extension[1]}".replace(" ", "")
        dict_of_files[file] = full_time_of_create
    return dict_of_files
