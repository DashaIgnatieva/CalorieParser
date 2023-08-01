# Функции для записи и чтения html документов

def write_html(data, name, encoding = 'utf-8'):
    with open(f'{name}.html', 'w', encoding=encoding) as file:
        file.write(data)
        file.close()

def read_html(name, encoding='utf-8'):
    with open(f'{name}.html', 'r', encoding=encoding) as file:
        data_for_work = file.read()
    return data_for_work