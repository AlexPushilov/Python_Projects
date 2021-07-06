import os


def replace_on_date(dictionary, way):
    """Эта фунция заменяет файлы и папки на дату их создания"""

    os.chdir(way)

    count = 0
    for file in os.listdir(way):
        if dictionary[file] in os.listdir(way):
            os.replace(file, f"{dictionary[file]}({count})")
        else:
            os.replace(file, dictionary[file])
        count += 1
