import random

def generate_array(size, lower_bound, upper_bound):
    """Генерация массива случайных чисел."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

if __name__ == "__main__":
    # Тестирование функции
    print(generate_array(5, 1, 100))
