import pandas as pd
import yaml
import xml.etree.ElementTree as ET

print("Привет! Давайте решим задачу по парсингу файла\
 и подсчету топ-10 самых повторяющихся слов длиннее шести символов с помощью Pandas.")

task = int(input("Выберите задачу парсинга (1 - JSON, 2 - XML, 3 - CSV, 4 - YAML): "))

if task == 1:
    file_name = input("Введите имя файла в формате JSON (например, newsafr.json): ")
    df_json = pd.read_json(r'\parser\newsafr.json')
    all_news_json = df_json['description'].str.split().explode()
    top_words_json = all_news_json[all_news_json.str.len() > 6].value_counts().head(10)
    print("ТОП 10 самых повторяющихся слов длиннее шести символов в файле JSON:")
    print(top_words_json)
elif task == 2:
    file_name = input("Введите имя файла в формате XML (например, newsafr.xml): ")
    tree = ET.parse(r'\parser\newsafr.xml')
    root = tree.getroot()
    descriptions = []
    for item in root.findall('.//item'):
        description = item.find('description').text
        descriptions.append(description)
    df = pd.DataFrame(descriptions, columns=['description'])
    all_news_xml = df['description'].str.split().explode()
    top_words_xml = all_news_xml[all_news_xml.str.len() > 6].value_counts().head(10)
    print("ТОП 10 самых повторяющихся слов длиннее шести символов в файле XML:")
    print(top_words_xml)
elif task == 3:
    file_name = input("Введите имя файла в формате CSV (например, newsafr.csv): ")
    df_csv = pd.read_csv(r'\parser\newsafr.csv')
    all_news_csv = df_csv['description'].str.split().explode()
    top_words_csv = all_news_csv[all_news_csv.str.len() > 6].value_counts().head(10)
    print("ТОП 10 самых повторяющихся слов длиннее шести символов в файле CSV:")
    print(top_words_csv)
elif task == 4:
    file_name = input("Введите имя файла в формате YAML (например, newsafr.yml): ")
    with open(r'\parser\newsafr.yml', 'r') as file:
        data = yaml.safe_load(file)
    df_yaml = pd.json_normalize(data, 'rss.channel.items')
    all_news_yaml = df_yaml['description'].str.split().explode()
    top_words_yaml = all_news_yaml[all_news_yaml.str.len() > 6].value_counts().head(10)
    print("ТОП 10 самых повторяющихся слов длиннее шести символов в файле YAML:")
    print(top_words_yaml)
else:
    print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 4.")