import configparser

config = configparser.ConfigParser()
config.read('config_for_parser.ini')

# Адрес сайта, выбранного для парсинга
site_url = config['url']['site_url']

print(site_url)