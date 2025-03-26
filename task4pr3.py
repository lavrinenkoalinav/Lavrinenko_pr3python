def format_number(input_number, decimal_places=2):
    try:
        number = float(input_number)
        return f"Відформатоване число: {number:.{decimal_places}f}"
    except ValueError:
        return "Помилка: Введене значення не є числом."

print(format_number("3.1415926535", 4))
