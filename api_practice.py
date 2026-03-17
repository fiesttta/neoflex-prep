import requests

# указываем url
url = "https://dummyjson.com/products/1"

print(f"Отправление GET-запроса на {url}...")

# сам GET запрос
response = requests.get(url)

# проверка статус-кода ответа
print(f"Статус сервера: {response.status_code}")

if response.status_code == 200:
    # переводим ответ в словарь
    data = response.json()

    print("\n--- Полученные данные ---")
    print(f"Название: {data['title']}")
    print(f"Описание: {data['description']}")
    print(f"Цена: {data['price']} $")

else:
    print("Что-то пошло не так.")
    