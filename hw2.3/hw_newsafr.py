import json
import chardet
from pprint import pprint


def get_data():
    with open('newsafr.json') as f:
        json_data = json.load(f)
        dict_news = json_data["rss"]["channel"]["items"]
    return dict_news


def get_list_of_words():
    d_news = get_data()
    list_of_words = []
    for items in d_news:
        news = items["description"]
        news_list = news.split()
        for word in news_list:
            lengh = len(word)
            if lengh > 6:
                list_of_words.append(word)
    return list_of_words


def get_wordfreq():
    list_of_words = get_list_of_words()
    wordfreq = [list_of_words.count(w) for w in list_of_words]

    return wordfreq


def get_popular_word():
    list_of_words = get_list_of_words()
    wordfreq = get_wordfreq()
    draft = list(zip(list_of_words, wordfreq))
    draft_one = set(draft)
    sort_draft = sorted(draft_one, key=lambda x: x[1], reverse=True)
    popular = sort_draft[:10]
    pprint(popular)


get_popular_word()



# with open ('newsafr.json') as f:
# 	json_data = json.load(f)
# 	dict_news = json_data["rss"]["channel"]["items"]

# list_of_words = []
# for items in dict_news:
# 	news = items["description"]
# 	news_list = news.split()
# 	for word in news_list:
# 		lengh = len(word)
# 		if lengh > 6:
# 			list_of_words.append(word)

# wordfreq = [list_of_words.count(w) for w in list_of_words]

# draft = list(zip(list_of_words, wordfreq))
# draft_one = set(draft)
# sort_draft = sorted(draft_one, key=lambda x: x[1], reverse=True)
# popular = sort_draft[:10]
# pprint(popular)
