import sqlite3

# Подключаемся к бд
connection = sqlite3.connect('store.db')
cursor = connection.cursor()

# Запрос на выборку всех данных
print("--- Видеокарты на складе (в наличии) ---")
cursor.execute("SELECT * FROM gpus WHERE in_stock = 1")

# Перехват результатов с курсора в переменную
all_gpus = cursor.fetchall()

# Проходимся по списку и печатаем
for gpu in all_gpus:
    print(f"[{gpu[0]}] Видеокарта: {gpu[1]} | Цена: {gpu[2]} руб.")

# закрытие соединения
connection.close()