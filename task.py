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

# Сортировка массива
def sort_arrays(arr1, arr2):
    arr1.sort(reverse=True)  # сортировка по убыванию
    arr2.sort()  # сортировка по возрастанию
    return arr1, arr2

# Тестирование
if __name__ == "__main__":
    arr1 = create_array()
    arr2 = create_array()
    arr1, arr2 = sort_arrays(arr1, arr2)
    print("Отсортированный массив 1:", arr1)
    print("Отсортированный массив 2:", arr2)
