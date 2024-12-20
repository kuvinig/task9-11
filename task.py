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

# Диалог создания массива
def create_array():
    choice = input("Выберите источник данных: 1 - Генерация, 2 - Ввод вручную: ")
    if choice == '1':
        size = int(input("Введите размер массива: "))
        arr = generate_array(size)
        print("Сгенерированный массив:", arr)
    elif choice == '2':
        arr = input_array()
        print("Введенный массив:", arr)
    else:
        print("Неверный выбор")
        return create_array()
    return arr

# Тестирование функции
if __name__ == "__main__":
    arr = create_array()
