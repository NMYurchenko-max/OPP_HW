import json
import xml.etree.ElementTree as ET
import csv
import yaml

def words_count(news):
    """
    Функция для подсчета повторяющихся слов длиннее шести символов в списке слов.
    Аргументы:
    news (list): Список слов для анализа.
    Возвращает:
    list: Список топ-10 самых повторяющихся слов.

    """
    length = 6
    top = 10
    news_dict = dict()
    top_ten = list()

    # Подсчет повторяющихся слов длиннее шести символов
    for word in news:
        if len(word) > length:
            news_dict[word] = 1

    for word in news:
        if word in news_dict.keys():
            news_dict[word] += 1

    # Сортировка значений словаря по убыванию
    freq = sorted(list(news_dict.values()), reverse=True)

    for k, v in news_dict.items():
        if v in (freq[0:(top)]):
            top_ten.extend(k.split())
        elif len(top_ten) == top:
            break

    return top_ten

# Задача №1 программа для файла в формате json
# Открываю файл, по ключу items нахожу список словарей с новостями
with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)
    json_news = json_data['rss']['channel']['items']

    # Создаю пустой список и складываю в него все слова,
    # входящие в описание каждой новости.
    # В каждом словаре это текстовое значение по ключу description
    all_news_json = list()
    for item in json_news:
        all_news_json.extend(item['description'].split())

    # Вызываю функцию words_count для списка слов, полученного из файла json
    print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
     в файле {f.name}:\n {words_count(all_news_json)}')
print('\n')

# Задача №2. программа для файла в формате XML
# Открываю файл XML
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)

# С помощью tree.getroot() получаю корневой элемент дерева
# XML (основной тег)
root = tree.getroot()

# С помощью root.findall() получаю все новости <item>,
# расположенные под тегом <channel>
xml_data = root.findall('channel/item')

# Создаю пустой список и складываю в него все слова,
# входящие в описание каждой новости.
# Описание новостей находится в тексте <description> под каждым тегом <item>
all_news_xml = list()
for news in xml_data:
    all_news_xml.extend(news.find('description').text.split())

# Вызываю функцию words_count для списка слов, полученного из файла xml
print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
 в файле XML:\n {words_count(all_news_xml)}')
print('\n')

# Задача №3 программа для файла в формате CSV

with open('newsafr.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    all_news_csv = list()
    for row in csv_reader:
        all_news_csv.extend(row['description'].split())
    print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
     в файле  CSV:\n {words_count(all_news_csv)}')
print('\n')

# Задача №4

with open('newsafr.yml', encoding='utf-8') as f:
    yaml_data = yaml.safe_load(f)
    yaml_news = yaml_data['rss']['channel']['items']
    all_news_yaml = list()
    for item in yaml_news:
        all_news_yaml.extend(item['description'].split())
    print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
     в файле YAML:\n {words_count(all_news_yaml)}')

print('\n')

print("Интерфейс пользователя: ")
# Приветствие
print("Привет! Давайте решим задачу по парсингу файла и подсчету топ-10 самых повторяющихся слов длиннее шести символов.")

# Запрос задачи парсинга
task = int(input("Выберите задачу парсинга (1 - JSON, 2 - XML, 3 - CSV, 4 - YAML): "))

# Решение задачи в зависимости от выбора
if task == 1:
    file_name = input("Введите имя файла в формате JSON (например, newsafr.json): ")
    with open('newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)
        json_news = json_data['rss']['channel']['items']
        all_news_json = list()
        for item in json_news:
            all_news_json.extend(item['description'].split())
        print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
         в файле {f.name}:\n {words_count(all_news_json)}')
    print('\n')
elif task == 2:
    file_name = input("Введите имя файла в формате XML (например, newsafr.xml): ")
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    xml_data = root.findall('channel/item')
    all_news_xml = list()
    for news in xml_data:
        all_news_xml.extend(news.find('description').text.split())
    print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
     в файле XML:\n {words_count(all_news_xml)}')
    print('\n')
elif task == 3:
    file_name = input("Введите имя файла в формате CSV (например, newsafr.csv): ")
    with open('newsafr.csv', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        all_news_csv = list()
        for row in csv_reader:
            all_news_csv.extend(row['description'].split())
        print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
         в файле  CSV:\n {words_count(all_news_csv)}')
elif task == 4:
    file_name = input("Введите имя файла в формате YAML (например, newsafr.yml): ")
    with open('newsafr.yml', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
        yaml_news = yaml_data['rss']['channel']['items']
        all_news_yaml = list()
        for item in yaml_news:
            all_news_yaml.extend(item['description'].split())
        print(f'ТОП 10 самых повторяющихся слов длиннее шести символов\
         в файле YAML:\n {words_count(all_news_yaml)}')

else:
    print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 4.")
