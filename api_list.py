import requests

# указываем url
url = "https://dummyjson.com/products"

print(f"Отправление GET-запроса на {url}...")

# сам GET запрос
response = requests.get(url)

# проверка статус-кода ответа
print(f"Статус сервера: {response.status_code}")

if response.status_code == 200:
    # переводим ответ в словарь
    data = response.json()
    print("\n--- Товары дороже 50 долларов ---")
    # достаем список по ключу products
    products_list = data['products']
    for product in products_list:
        if product['price'] > 50:

            print(f"Название: {product['title']}")
            print(f"Описание: {product['description']}")
            print(f"Цена: {product['price']} $")

else:
    print("Что-то пошло не так.")
    