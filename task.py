import random


# Генерация массива случайных чисел
def generate_array(size, lower_bound=1, upper_bound=100):
    """
    Генерирует массив случайных целых чисел.

    :param size: Размер массива.
    :param lower_bound: Нижняя граница чисел (по умолчанию 1).
    :param upper_bound: Верхняя граница чисел (по умолчанию 100).
    :return: Список случайных чисел в диапазоне от lower_bound до upper_bound.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


# Ручной ввод массива
def input_array():
    """
    Запрашивает у пользователя ввод массива вручную.

    :return: Список чисел, введенных пользователем.
    """
    size = int(input("Введите размер массива: "))
    array = []
    for i in range(size):
        number = int(input(f"Введите элемент массива {i + 1}: "))
        array.append(number)
    return array


# Диалог создания массива
def create_array():
    """
    Позволяет пользователю выбрать способ создания массива: генерация случайных чисел или ввод вручную.

    :return: Массив чисел, созданный выбранным методом.
    """
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


# Сортировка массивов
def sort_arrays(arr1, arr2, arr3):
    """
    Сортирует три массива: первый и третий по убыванию, второй по возрастанию.

    :param arr1: Первый массив.
    :param arr2: Второй массив.
    :param arr3: Третий массив.
    :return: Отсортированные массивы.
    """
    arr1.sort(reverse=True)  # сортировка по убыванию
    arr2.sort()  # сортировка по возрастанию
    arr3.sort(reverse=True)  # сортировка по убыванию для третьего массива
    return arr1, arr2, arr3


# Задание 10 - Проверка арифметических операций между элементами массивов
def task_10(array1, array2, array3):
    """
    Проверяет, можно ли получить числа из 3 массива с помощью арифметических преобразований
    элементов двух других массивов.

    :param array1: Первый массив.
    :param array2: Второй массив.
    :param array3: Третий массив, проверяемый на совпадение.
    :return: Список булевых значений, показывающих, можно ли получить число из array3.
    """
    result = []

    for a1, a2, a3 in zip(array1, array2, array3):
        if a1 + a2 == a3 or a1 - a2 == a3 or a1 * a2 == a3 or (a2 != 0 and a1 / a2 == a3):
            result.append(True)
        else:
            result.append(False)

    return result


# Основное меню
def main_menu():
    """
    Основное меню программы, предлагающее выбор задания или завершение работы.
    """
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
