# Функции необходимые для работы с базой данных SQLite.
import sqlite3

class DataBase:

    def __init__(self, db_name):
        self.connection = sqlite3.connect(f'{db_name}.db')
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str):

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
        productId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        product TEXT,
        calories REAL,
        proteins REAL,
        fats REAL,
        carbs REAL,
        category TEXT)
        """)

        self.connection.commit()

    def write_to_table(self, product_info: list):
        product_name, product_calories, product_proteins, product_fats, product_carbs, product_category = product_info

        self.cursor.execute(f"""INSERT INTO products(product, calories, proteins, fats, carbs, category) 
        VALUES('{product_name}', '{product_calories}', '{product_proteins}', '{product_fats}', '{product_carbs}', '{product_category}');""")
        
        self.connection.commit()

    def cursor_close(self):
        self.cursor.close()