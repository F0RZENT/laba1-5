input_string = input("Введите строку: ")

lowercase_count = sum(1 for char in input_string if char.islower())
uppercase_count = sum(1 for char in input_string if char.isupper())

print(f"Количество больших букв: {lowercase_count}")
print(f"Количество маленьких букв: {uppercase_count}")