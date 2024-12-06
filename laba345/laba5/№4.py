D = [10, 20, 30, 40, 50, 60, 70, 80]

sum_odd_indices = sum(D[i] for i in range(1, len(D), 2))

print("Список D:", D)
print("Сумма элементов с нечетными индексами:", sum_odd_indices)