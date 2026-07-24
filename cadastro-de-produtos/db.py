
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'database.sqlite3'
DB_FILE =  ROOT_DIR / DB_NAME
TABLE_NAME = 'produtos'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name_product TEXT,'
    'preço REAL,'
    'estoque INT'
    ')'
)
connection.commit()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}' 
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name_product, preço, estoque) '
    'VALUES '
    '(:name_product, :preço, :estoque)' 
)
connection.commit()


if __name__ == '__main__':
    cursor.close()
    connection.close()

# if __name__ == '__main__':
    # print(sql)
    
    # cursor.execute( # FAZENDO DELETE NA TABELA
    # f'DELETE FROM {TABLE_NAME} '
    # 'WHERE id = "3"'
    # )
    # cursor.execute( # FAZENDO DELETE NA TABELA
    #     f'DELETE FROM {TABLE_NAME} '
    #     'WHERE id = "1"'
    # )
    # cursor.execute(
    #     f'UPDATE  {TABLE_NAME} ' # no UPDATE preciso saber qual id estou atualizando no WHERE, e preciso saber qual campo/coluna q estou utilizando, para qual valor essa coluna vai
    #     'SET name = "QUALQUER", weight = 67.89 '
    #     'WHERE id = "2"'
    # )
    # connection.commit()

    # cursor.execute(
    # f'SELECT * FROM {TABLE_NAME} '
    # )
    
    # for row in cursor.fetchall(): 
    #     _id, name, weight = row
    #     print(_id, name, weight)