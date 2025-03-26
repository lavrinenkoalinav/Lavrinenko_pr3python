def arithmetic_operations(str_num1, str_num2):
    try:
        num1, num2 = float(str_num1), float(str_num2)
        return (f"Сума: {num1 + num2}\n"
                f"Різниця: {num1 - num2}\n"
                f"Добуток: {num1 * num2}\n"
                f"Частка: {num1 / num2 if num2 != 0 else 'Помилка: ділення на нуль'}")
    except ValueError:
        return "Помилка: Введені значення мають бути числами."

print(arithmetic_operations("12", "4"))
