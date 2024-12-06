input_string = input("Введите строку из слов, разделенных пробелами: ")

words = input_string.split()

if len(words) == 0:
    print("Ошибка: строка пуста.")
else:
    longest_word = max(words, key=len)
    print(f"Самое длинное слово: {longest_word}")