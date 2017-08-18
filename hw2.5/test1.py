AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6118540
VERSION = '5.67'

auth_data = [
    'client_id': APP_ID,
    'redirect_url': 'https://oauth.vk.com/blank.html',
    'display': 'mobile',
    'scope': 'friends',
    'response_type': 'token',
    'v': VERSION

]

print('?'.join(
    (AUTHORIZE_URL, urlencode(auth_data))
))