import requests
import sqlite3

# extract (извлекаем данные из api)

print("Стучимся в api...")
url = "https://dummyjson.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    products_list = data["products"]
    print(f"Получено товаров: {len(products_list)}")
else:
    print("Ошибка сети.")
    exit()

# готовим базу данных
print("\nСоздание базы данных pr_store.db...")
connection = sqlite3.connect("pr_store.db")
cursor = connection.cursor()

# создаем таблицу для товаров
cursor.execute('''
CREATE TABLE IF NOT EXISTS api_products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
price REAL
)
''')

# защита от дубляжа
cursor.execute('DELETE FROM api_products')

# transform and load (фильтруем и заполняем)
print("Сохраняем товары дороже 50$ в базу данных...")

inserted_count = 0
for product in products_list:
    if product['price'] > 50:
        cursor.execute('''
        INSERT INTO api_products (title, price)
        VALUES (?, ?)
        ''', (product['title'], product['price']))

        inserted_count += 1

# сохранение изменений
connection.commit()
print(f"Успех. В базу записано {inserted_count} товаров дороже 50$")

# select (проверка)
print("\n--- Проверяем какие товары находятся в базе данных ---")

cursor.execute("SELECT title, price FROM api_products")
for row in cursor.fetchall():
    print(f"Товар: {row[0]} | Цена: {row[1]}$")

connection.close()