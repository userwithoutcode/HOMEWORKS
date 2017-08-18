import requests
import os


def open_file(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        text = f.read()
    return text


def define_lang(text):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/detect ?
    key=<API-ключ>
     & text=<текст>
     & [hint=<список вероятных языков текста>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for detect.
    :return: <str> lang text.
    """

    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    key = 'trnsl.1.1.20170718T141601Z.5e501527846260fe.7190b2f8743d55f7468442c1da1aced320d2af6c'

    params = {
        'key': key,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return response.get('lang')


def translate_it(text, lang_source, d_lang='ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20170718T141601Z.5e501527846260fe.7190b2f8743d55f7468442c1da1aced320d2af6c'

    lang = lang_source + '-' + d_lang

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def write_to_file(text, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        f.write(text)


def main_function():
    file_list = ['DE.txt', 'ES.txt', 'FR.txt']
    for file_name in file_list:
        name, extension = os.path.splitext(file_name)
        text = open_file(file_name)
        lang_source = define_lang(text)
        text_translate = translate_it(text, lang_source)
        name_result = name + '_RU.txt'
        write_to_file(text_translate, name_result)

main_function()
