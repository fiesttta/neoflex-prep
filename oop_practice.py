class VideoCard:
    # Метод __init__ вызывается автоматически при создании объекта. 
    # Он задает начальные характеристики (атрибуты).
    def __init__(self, model, memory, temperature):
        self.model = model
        self.memory = memory
        self.__temperature = temperature

    # Это метод (функция, которая принадлежит классу)
    def cool_down(self):
        print(f"Вентиляторы раскручиваются... Температура {self.model} падает!")
        self.__temperature -= 10

    def overclock(self):
        print(f"Внимание! Разгоняем {self.model}")
        self.__temperature += 20
    
    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temp):
        if 120 < new_temp or new_temp < 20:
            print("Ошибка: недопустимая температура!")
        else: 
            self.__temperature = new_temp

# Создаем конкретный объект (твою видеокарту) по "чертежу" VideoCard
my_gpu = VideoCard(model="RTX 3060 Ti", memory=8, temperature=60)

# Проверяем атрибуты
print(f"Моя видеокарта: {my_gpu.model}, Температура: {my_gpu.get_temperature()} градусов.")

# Вызываем метод
my_gpu.cool_down()


# Проверяем температуру после охлаждения
print(f"Температура после охлаждения: {my_gpu.get_temperature()} градусов.")

# Вызываем метод разгона
my_gpu.overclock()

# Проверяем температуру после разгона
print(f"Температура после разгона: {my_gpu.get_temperature()} градусов")

# Пытаемся сжечь видеокарту
my_gpu.set_temperature(500)

# Проверям температуру (смогли ли сжечь)
print(f"Текущая температура {my_gpu.get_temperature()} градусов.")

# Новый класс наследник от VideoCard
class IntegratedGPU(VideoCard):
    def __init__(self, model, memory, temperature):
        super().__init__(model, memory, temperature)

    # Метод забирающий часть ОЗУ
    def share_ram(self):
        print(f"Встроенная графика {self.model} забирает часть ОЗУ под свои нужды!")

# Создаем конкретный объект (встроенную видеокарту) по "чертежу" IntegratedGPU
my_laptop_gpu = IntegratedGPU(model="AMD Radeon Vega", memory=0, temperature= 63)

# Охлаждаем родительским методом
my_laptop_gpu.cool_down()

# Проверяем температуру после охлаждения
print(f"Температура после охлаждения: {my_laptop_gpu.get_temperature()} градусов.")

# Вызываем метод
my_laptop_gpu.share_ram()