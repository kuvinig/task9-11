def input_array(size):
    """Ввод массива пользователем."""
    array = []
    print(f"Введите {size} чисел:")
    for _ in range(size):
        number = int(input("Введите число: "))
        array.append(number)
    return array

if __name__ == "__main__":
    # Тестирование функции
    print(input_array(5))
