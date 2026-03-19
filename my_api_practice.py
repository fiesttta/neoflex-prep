from fastapi import FastAPI
import sqlite3

# создание веб сервера
app = FastAPI()

# URL по которому будет доступна функция
@app.get("/")
def read_root():
    return {"message": "Вы попали в API магазина"}

# URL отдающий данные из бд
@app.get("/api/products")
def get_products():
    # подключаемся к бд
    connection = sqlite3.connect("pr_store.db")
    cursor = connection.cursor()

    # достаем товары
    cursor.execute("SELECT title, price FROM api_products")

    # собираем список словарей (JSON)
    products_list = []
    for row in cursor.fetchall():
        products_list.append({
            "title": row[0],
            "price": row[1]
        })

    connection.close()

    return {"products": products_list}