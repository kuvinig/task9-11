import random

# Генерация массива случайных чисел
def generate_array(size, lower_bound=1, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Ручной ввод массива
def input_array():
    size = int(input("Введите размер массива: "))
    array = []
    for i in range(size):
        number = int(input(f"Введите элемент массива {i + 1}: "))
        array.append(number)
    return array

# Тестирование функций
if __name__ == "__main__":
    # Выбор источника данных
    choice = input("Выберите источник данных: 1 - Генерация, 2 - Ввод вручную: ")
    if choice == '1':
        arr = generate_array(10)
        print("Сгенерированный массив:", arr)
    elif choice == '2':
        arr = input_array()
        print("Введенный массив:", arr)
