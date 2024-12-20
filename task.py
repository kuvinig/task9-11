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
def sort_arrays(arr1, arr2, arr3):
    arr1.sort(reverse=True)  # сортировка по убыванию
    arr2.sort()  # сортировка по возрастанию
    arr3.sort(reverse=True)  # сортировка по убыванию для третьего массива
    return arr1, arr2, arr3

# Задание 10 - Проверка арифметических операций между элементами массивов
def task_10(array1, array2, array3):
    """Проверка, можно ли получить числа из 3 массива с помощью арифметических преобразований двух других массивов."""
    result = []

    for a1, a2, a3 in zip(array1, array2, array3):
        if a1 + a2 == a3 or a1 - a2 == a3 or a1 * a2 == a3 or (a2 != 0 and a1 / a2 == a3):
            result.append(True)
        else:
            result.append(False)

    return result

# Основное меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Задание 10")
        print("2 - Завершить программу")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            arr1 = create_array()
            arr2 = create_array()
            arr3 = create_array()
            arr1, arr2, arr3 = sort_arrays(arr1, arr2, arr3)
            result = task_10(arr1, arr2, arr3)
            print("Результат выполнения алгоритма:", result)
        elif choice == '2':
            print("Завершение программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main_menu()
