"""
Вариант 2 решения Задача 3:

@author: Nina
"""
import os

# Проверка рабочей директории
working_directory = os.getcwd()
print(os.getcwd())

# Определение пути к папке с файлами относительно рабочей директории
folder_name = 'source_files'

# Используем относительный путь к директории
relative_folder_path = os.path.join(working_directory, folder_name)

# Проверка существования директории
if not os.path.exists(relative_folder_path):
    print(f"Директория '{relative_folder_path}' не найдена.\
         Проверьте существование директории и попробуйте снова.")
    exit(1) # Завершаем программу с кодом ошибки

# Обработка исходных файлов и вывод посторочно на печать
files = os.listdir(relative_folder_path)
files.sort()

for idx, file_name in enumerate(files, start=1):
    with open(os.path.join(relative_folder_path, file_name), 'r', encoding='utf-8') as file:
        print(f'Файл номер {idx}: {file_name}')
        for line_num, line in enumerate(file, start=1):
            print(f'Строка номер {line_num} файла номер {idx}: {line.strip()}')
        print()

# Объединение файлов с записью в один итоговый по заданным параметрам
files.sort(key=lambda x: sum(1 for line in open(os.path.join(relative_folder_path, x), encoding='utf-8')))
final_file_path = os.path.join(relative_folder_path, 'merge_file.txt')

with open(final_file_path, 'w', encoding='utf-8') as final_file:
    for file_name in files:
        with open(os.path.join(relative_folder_path, file_name), 'r', encoding='utf-8') as file:
            final_file.write(file.read())

print('Файлы успешно объединены в merge_file.txt')
print(f'Путь к объединенному файлу: {final_file_path}', "файл по окончанию\
     программы будет перемещен в рабочую директорию")

# Печать содержимого итогового файла
print('\nСодержание объединенного файла "merge_file.txt":')
with open(final_file_path, 'r', encoding='utf-8') as final_file:
    for line in final_file:
        print(line.strip())

# Перемещение итогового файла из папки с исходными с заменой
existing_file_path = os.path.join('files', 'merge_file.txt')

if os.path.isfile(final_file_path):
    os.replace(final_file_path, existing_file_path)

print('Файл merge_file.txt успешно перемещен в папку files.')