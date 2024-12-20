import random

# Генерация массива случайных чисел
def generate_array(size, lower_bound=1, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Тестирование функции
if __name__ == "__main__":
    arr = generate_array(10)
    print("Сгенерированный массив:", arr)
