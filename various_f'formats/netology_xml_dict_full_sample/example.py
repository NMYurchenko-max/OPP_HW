import requests
import codecs

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(file_path, result_path, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param file_path:
    :param from_lang:
    :param to_lang:
    :param result_path:
    :return:
    """

    with open(file_path, 'r') as f:
        data = f.read().strip()

    params = {
        'key': API_KEY,
        'text': data,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with codecs.open(f'translated-to-{to_lang}-{result_path}', 'w', 'utf-8') as file:
        file.write(''.join(json_['text']))


files = ['DE.txt', 'ES.txt', 'FR.txt']

for item in files:
    file_lang = item.split('.')[0].lower()
    result = item
    translate_it(file_path=item, from_lang=file_lang, result_path=result)
