from pathlib import Path
import shutil



# Получение текущей рабочей директории и пути к папке с исходными файлами
working_directory = Path.cwd()
folder_path = Path('read_write/source_files')

# Обработка файлов в папке
# Определение списка имен исходных файлов
file_names = [file.name for file in folder_path.iterdir() if file.is_file()]

# Сначала считаем количество строк в каждом файле
file_info = {}
for file_name in file_names:
    with open(folder_path.joinpath(file_name), 'r', encoding='utf-8') as file:
        lines = sum(1 for _ in file)
        file_info[file_name] = lines

# Создаем список кортежей с именами файлов и количеством строк
file_list = [(file_name, file_info[file_name]) for file_name in file_names]

# Сортируем список кортежей по количеству строк
sorted_files = sorted(file_list, key=lambda x: x[1])

# Вывод информации о файлахах и их содержании 
for idx, file_name in enumerate(file_names, start=1):
    with open(folder_path.joinpath(file_name), 'r', encoding='utf-8') as file:
        print(f'Файл номер {idx}: {file_name}')
        for line_num, line in enumerate(file, start=1):
            print(f'Строка номер {line_num} файла номер {idx}: {line.strip()}')
        print()

# Затем объединяем файлы, добавляя информацию об источнике и количестве строк
final_file_path = folder_path / 'final_file.txt'

with open(final_file_path, 'w', encoding='utf-8') as final_file:
    for file_name, lines in sorted_files:
        with open(folder_path.joinpath(file_name), 'r', encoding='utf-8') as file:
            final_file.write(f"Источник: {file_name}\n Количество строк: {lines}\n")
            final_file.write(file.read())
            final_file.write('\n' + '---' + '\n') # Добавляем разделитель между файлами

print('Файлы успешно объединены в final_file.txt')

# Получение текущей рабочей директории
working_directory = Path.cwd()

# Путь к итоговому файлу в папке source_files
source_file_path = working_directory / 'read_write/source_files' / 'final_file.txt'

# Создание пути к итоговому файлу в рабочей директории
destination_file_path = working_directory / 'read_write/files' / 'final_file.txt'

# Перемещение итогового файла в рабочую директорию
shutil.move(source_file_path, destination_file_path)

# Получение относительного пути к итоговому файлу
relative_path = destination_file_path.relative_to(working_directory)

# Печать сообщения об успешном перемещении итогового файла
print('Файл final_file.txt успешно перемещен в корневую рабочую директорию.')
""" Проверка перемещения итогового файла в рабочую директорию
    Если выводится правильный путь, значит перемещение прошло успешно
"""
print(f'Путь к объединенному файлу: {relative_path}')
# Печать содержимого итогового файла
print('\nСодержимое итогового файла "final_file.txt":')
with open(relative_path, 'r', encoding='utf-8') as final_file:
    for line in final_file:
        print(line.strip())