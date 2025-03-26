def list_conversion(input_str):
    try:
        numbers = list(map(float, input_str.split(",")))
        return f"Сума: {sum(numbers)}\nСереднє значення: {sum(numbers) / len(numbers)}"
    except ValueError:
        return "Помилка: Невірний формат введення. Використовуйте коми для розділення чисел."

print(list_conversion("1, 2, 3, 4, 5"))
