import json
import chardet


def decoding_file(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    return result['encoding']


def open_file(file_name, encoding_type):
    with open(file_name, encoding=encoding_type) as f:
        data = json.load(f)

        list_words = []
        dict_news = {}

        for text_news in data['rss']['channel']['items']:
            list_words += (text_news['title']).split()
            list_words += (text_news['description']).split()
        for word in list_words:
            if len(word) < 6:
                continue
            else:
                if word.lower() not in dict_news:
                    dict_news[word.lower()] = int(list_words.count(word))

    return dict_news


def popular_words(dict_news):
    rev_dict_news = (dict(reversed((sorted(dict_news.items(), key=lambda item: item[1])))))
    rev_dict_news_sorted = {}
    for key, value in rev_dict_news.items():
        if len(rev_dict_news_sorted) < 10:
            rev_dict_news_sorted[key] = value
    for key, value in rev_dict_news_sorted.items():
        print('{1} - {0}'.format(key, value))
    print('\n')


def main_function():
    file_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    for file_name in file_list:
        encoding_type = decoding_file(file_name)
        count_dict = open_file(file_name, encoding_type)
        popular_words(count_dict)

main_function()