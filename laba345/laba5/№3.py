my_list = [10, -5, 20, -1, 30, -10, 0]

positive_numbers = [num for num in my_list if num > 0]
non_positive_numbers = [num for num in my_list if num <= 0]

print("Положительные числа:", positive_numbers)
print("Остальные числа (ноль или отрицательные):", non_positive_numbers)