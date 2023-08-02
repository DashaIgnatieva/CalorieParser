from configs import site_url
from getter import get_site_code
import sys
from documents_creator import *
from bs4 import BeautifulSoup
from database import DataBase

headers = {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    site_data = get_site_code(site_url, headers)
    if site_data.status_code == 200:
        print(f'Соединение установлено, статус: {site_data.status_code}')
    else:
        print(f'Информация недоступна, код ошибки: {site_data.status_code}')
        sys.exit()        
except:
    print(f'Нет соединения')
    sys.exit()

write_html(site_data.text, 'site_data', encoding='ISO-8859-1')
data_for_work = read_html('site_data', encoding='Windows-1251')

soup = BeautifulSoup(data_for_work, 'lxml')

# Ниже я ищу сразу 2 тега. Так же указываю классы этих тегов
unsorted_data_for_table = soup.find_all(['div', 'table'], class_=['norm','z1'])

db_name = 'Products'
table_name = 'products'

products_db = DataBase(db_name)
products_db.create_table(table_name)

product_type_for_db = ''
for i in range(len(unsorted_data_for_table)):

    # В этом if мы парсим имя категории продуктов
    if unsorted_data_for_table[i].name == 'div':
        if unsorted_data_for_table[i].text.count('Таблица самых низкокалорийных продуктов питания'):
            continue

        if unsorted_data_for_table[i].text.count('Таблица самых калорийных продуктов питания'):
            continue

        product_type = unsorted_data_for_table[i].text
        product_type = product_type.split(':')
        product_type_for_db = product_type[0].strip()

    # В этом if мыпарсим данные о продукте и записываем их в бд
    if unsorted_data_for_table[i].name == 'table':
        if unsorted_data_for_table[i-1].text.count('Таблица самых низкокалорийных продуктов питания'):
            continue
        if unsorted_data_for_table[i-1].text.count('Таблица самых калорийных продуктов питания'):
            continue
        products_info = unsorted_data_for_table[i].find_all('tr')
        for product in products_info:
            if product.find_all('td', class_='norm_verh'):
                continue
            produkt_table_string = product.find_all('td')
            product_data = [produkt_table_string[0].text.lower(),
                            int(produkt_table_string[1].text),
                            float(produkt_table_string[2].text),
                            float(produkt_table_string[3].text),
                            float(produkt_table_string[4].text),
                            product_type_for_db.lower()]

            products_db.write_to_table(product_data)
            print(f'Продукт "{produkt_table_string[0].text}" из категории "{product_type_for_db}" записан')

products_db.cursor_close()
print(f'Запись таблицы "{table_name}" базы данных "{db_name}.db" завершена')