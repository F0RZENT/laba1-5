input_string = input()


if len(input_string) < 2:
    print("Ошибка: строка должна содержать минимум два символа.")
else:
    modified_string = "!" + input_string[1:-1] + "!"
    print(f"Преобразованная строка: {modified_string}")
