word = input("Введите слово: ")

if len(word) == 0:
    print("Ошибка: строка пуста.")
else:
    length = len(word)
    first_letter = word[0]
    last_letter = word[-1]

    print(f"Длина слова: {length}")
    print(f"Первая буква: {first_letter}")
    print(f"Последняя буква: {last_letter}")
