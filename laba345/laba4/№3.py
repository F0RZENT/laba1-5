# Ввод максимальной длины строки
k = int(input("Введите максимально возможную длину строки (k): "))

# Ввод произвольной строки
input_string = input("Введите произвольную строку: ")

# Проверяем длину строки
if len(input_string) > k:
    # Извлекаем "лишние" символы
    extra_chars = input_string[k:]
    # Обрезаем строку до допустимой длины
    truncated_string = input_string[:k]
    print(f"Укороченная строка: {truncated_string}")
    print(f"Лишние символы: {extra_chars}")
else:
    print(f"Строка не превышает допустимую длину: {input_string}")