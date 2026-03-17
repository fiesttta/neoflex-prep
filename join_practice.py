import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# Создаем таблицу производителей
cursor.execute('''
CREATE TABLE IF NOT EXISTS manufacturers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
country TEXT
)
''')

# Заполняем таблицу
cursor.execute('DELETE FROM manufacturers')
cursor.execute("INSERT INTO manufacturers (id, name, country) VALUES (1, 'Nvidia', 'USA')")
cursor.execute("INSERT INTO manufacturers (id, name, country) VALUES (2, 'AMD', 'USA')")

# Пересоздаем таблицу видеокарт
cursor.execute('DROP TABLE IF EXISTS gpus')

# Создаем уже с производителем 
cursor.execute('''
CREATE TABLE IF NOT EXISTS gpus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    price INTEGER,
    in_stock BOOLEAN,
    manufacturer_id INTEGER
)
''')

# Добавление трех моделей
cursor.execute("INSERT INTO gpus (model, price, in_stock, manufacturer_id) VALUES ('RTX 3060 Ti', 40000, 1, 1)")
cursor.execute("INSERT INTO gpus (model, price, in_stock, manufacturer_id) VALUES ('RTX 4090', 150000, 0, 1)")
cursor.execute("INSERT INTO gpus (model, price, in_stock, manufacturer_id) VALUES ('AMD Radeon Vega', 0, 1, 2)")

connection.commit()

print("--- Видеокарты с указанием бренда ---")

# Склеиваем
cursor.execute('''
SELECT gpus.model, manufacturers.name, gpus.in_stock, gpus.price
FROM gpus
INNER JOIN manufacturers ON gpus.manufacturer_id = manufacturers.id
''')

# Вывод
boolean_stock = ["Нет", "Да"]
for row in cursor.fetchall():
    print(f"Модель: {row[0]} | Производитель: {row[1]} | В наличии: {boolean_stock[row[2]]} | Цена: {row[3]} руб.")

connection.close()