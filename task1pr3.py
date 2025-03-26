def convert_and_calculate(input_str):
    try:
        number = float(input_str)
        result = number * 2  
        return str(result)
    except ValueError:
        return "Помилка: Введене значення не є числом."

input_value = "10.5"
print("Результат:", convert_and_calculate(input_value))
