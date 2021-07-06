from description_of_program import description, way
from exception import try_change_dir
from replace import replace_on_date
from dictionary import date_of_create

# Описание программы
description()

# Ввод пользователя
path = way()

# Проверка path на правильность
try_change_dir(path)

# Получаем словарь
dictionary = date_of_create(path)

# Меняем файлы на их время создания
replace_on_date(dictionary, path)

print("\nПрограмма завершена!")
