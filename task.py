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

# Алгоритм для задания 1
def task_1(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            result.append(0)
        else:
            result.append(arr1[i] + arr2[i])
    result.sort()  # сортировка результирующего массива по возрастанию
    return result

# Основное меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Задание 1")
        print("2 - Завершить программу")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            arr1 = create_array()
            arr2 = create_array()
            arr1, arr2 = sort_arrays(arr1, arr2)
            result = task_1(arr1, arr2)
            print("Результат выполнения алгоритма:", result)
        elif choice == '2':
            print("Завершение программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main_menu()
