import sqlite3

# Подключаемся к бд
connection = sqlite3.connect('store.db')
cursor = connection.cursor()

# Запрос на выборку всех данных
print("--- Все видеокарты на складе ---")
cursor.execute("SELECT * FROM gpus")

# Перехват результатов с курсора в переменную
all_gpus = cursor.fetchall()

# Проходимся по списку и печатаем
for gpu in all_gpus:
    print(gpu)

# закрытие соединения
connection.close()