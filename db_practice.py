import sqlite3

# Подключимя\создадим базу данных
connection = sqlite3.connect("store.db")

# Специальный объект отправляющий комманды
cursor = connection.cursor()

# Запрос на создание таблицы. Если уже есть, она не пересоздается
cursor.execute('''
CREATE TABLE IF NOT EXISTS gpus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    price INTEGER,
    in_stock BOOLEAN
)
''')

# Добавление данных в таблицу. Для начала очистим для избежания дублирования
cursor.execute('DELETE FROM gpus')

# Добавление трех моделей
cursor.execute("INSERT INTO gpus (model, price, in_stock) VALUES ('RTX 3060 Ti', 40000, 1)")
cursor.execute("INSERT INTO gpus (model, price, in_stock) VALUES ('RTX 4090', 150000, 0)")
cursor.execute("INSERT INTO gpus (model, price, in_stock) VALUES ('AMD Radeon Vega', 0, 1)")

# Сохранение изменений
connection.commit()

print("База данных успешно создана и заполнена.")

# Закритие соединения
connection.close()