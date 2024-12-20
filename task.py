def create_array():
    """Диалог выбора способа создания массива."""
    choice = input("Выберите способ ввода массива:\n1 - Ручной ввод\n2 - Генерация случайных чисел\nВведите 1 или 2: ")
    size = int(input("Введите размер массива: "))

    if choice == '1':
        return input_array(size)
    elif choice == '2':
        lower_bound = int(input("Введите нижний предел: "))
        upper_bound = int(input("Введите верхний предел: "))
        return generate_array(size, lower_bound, upper_bound)
    else:
        print("Неверный выбор!")
        return []


if __name__ == "__main__":
    # Тестирование функции
    print(create_array())
