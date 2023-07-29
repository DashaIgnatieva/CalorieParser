# Здесь находятся функции для получения html кода страницы, 
# которую мы будем парсить

import requests

def get_site_code(url, headers):
    page = requests.get(url=url, headers=headers)
    return page
