# from configs import site_url
from getter import get_site_code
import sys
from documents_creator import *
from bs4 import BeautifulSoup
from database import DataBase

# headers = {
#     "Accept":"*/*",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }

# try:
#     site_data = get_site_code(site_url, headers)
#     if site_data.status_code == 200:
#         print(f'Соединение установлено, статус: {site_data.status_code}')
#     else:
#         print(f'Информация не доступна, код ошибки: {site_data.status_code}')
#         sys.exit()        
# except:
#     print(f'Нет соединения')
#     sys.exit()

# write_html(site_data.text, 'site_data', encoding='ISO-8859-1')
data_for_work = read_html('site_data', encoding='Windows-1251')

soup = BeautifulSoup(data_for_work, 'lxml')

# Ниже я ищу сразу 2 тега. Так же указываю классы этих тегов
unsorted_data_for_table = soup.find_all(['div', 'table'], class_=['norm','z1'])

# Данные, которые будут записанны в таблицу
sorted_data_for_table = []

for i in range(len(unsorted_data_for_table)):
    if (unsorted_data_for_table[i].name == 'table'):
        continue
    if (unsorted_data_for_table[i].text.count("Таблица самых низкокалорийных продуктов питания")): 
        continue
    if (unsorted_data_for_table[i].text.count("Таблица самых калорийных продуктов питания")):
        continue

    sorted_data_for_table.append(unsorted_data_for_table[i+1])

products_db = DataBase('Products')

