# Функции для записи и чтения разноформатных документов

import json

def write_html(data, name, encoding = 'utf-8'):
    with open(f'{name}.html', 'w', encoding=encoding) as file:
        file.write(data)
        file.close()

def read_html(name, encoding='utf-8'):
    with open(f'{name}.html', 'r', encoding=encoding) as file:
        data_for_work = file.read()
    return data_for_work

def write_JSON(data, name):
    with open(f'{name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, ensure_ascii=False)
        file.close()

def read_JSON(name):
    with open(f'{name}.html', 'r', encoding='utf-8') as file:
        data_for_work = json.load(file)
    return data_for_work