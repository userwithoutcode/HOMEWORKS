from pprint import pprint
from urllib.parse import urlencode
import requests


def get_token():
    AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
    APP_ID = 'd549534118c545e2af9e6b5553aa8206'

    auth_data = {
        'response_type': 'token',
        'client_id': APP_ID
    }

    print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


TOKEN = 'AQAAAAAFjlMpAARz5VhlO_y_4kLyh0vcYwAG9bA'


class YandexMetrika:
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/counters/'
    headers = {
        'Authorization': 'OAuth {}'.format(TOKEN),
        'Content-Type': 'application/x-yametrika+json',
    }

    def __init__(self, token):
        self.token = token

    def get_counters(self):
        '''создаем словарь'''
        url = self.MANAGEMENT_URL
        headers = self.headers
        response = requests.get(url, headers=headers)
        counters = response.json()['counters']
        return dict(zip([counter['id'] for counter in counters],
                        [counter['name'] for counter in counters]))

    def get_visits_pageviews_users(self, count_id):
        """
         запрашиваем визиты, просмотры, кол-во пользовтелей
        """
        url = 'https://api-metrika.yandex.ru/stat/v1/data'
        headers = self.headers
        params = {
            'id': count_id,
            'metrics': 'ym:s:visits, ym:s:pageviews, ym:s:users'

        }
        response = requests.get(url, params, headers=headers)
        vpu = response.json()['totals']
        print(
            'Визитов {}\nПросмотров {}\nПользователей {}\n'.format(
                vpu[0], vpu[1], vpu[2]
            ))

    def get_counters_info(self):
        """
        Выводим всю информацию по счетчикам YM
        """
        for key, value in YMetrika.get_counters().items():
            print('Название: {}\n'
                  'Идентификатор: {}\n'.format(value, key))
            YMetrika.get_visits_pageviews_users(key)


YMetrika = YandexMetrika(TOKEN)
YMetrika.get_counters_info()
