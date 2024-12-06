input_string = input("Введите строку из двух слов через пробел: ")

words = input_string.split()

if len(words) != 2:
    print("Ошибка: строка должна содержать ровно два слова, разделенных пробелом.")
else:
    print(f"Второе слово: {words[1]}")