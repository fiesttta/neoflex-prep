class VideoCard:
    # Метод __init__ вызывается автоматически при создании объекта. 
    # Он задает начальные характеристики (атрибуты).
    def __init__(self, model, memory, temperature):
        self.model = model
        self.memory = memory
        self.temperature = temperature

    # Это метод (функция, которая принадлежит классу)
    def cool_down(self):
        print(f"Вентиляторы раскручиваются... Температура {self.model} падает!")
        self.temperature -= 10

# Создаем конкретный объект (твою видеокарту) по "чертежу" VideoCard
my_gpu = VideoCard(model="RTX 3060 Ti", memory=8, temperature=60)

# Проверяем атрибуты
print(f"Моя видеокарта: {my_gpu.model}, Температура: {my_gpu.temperature} градусов.")

# Вызываем метод
my_gpu.cool_down()

# Проверяем температуру после охлаждения
print(f"Температура после охлаждения: {my_gpu.temperature} градусов.")