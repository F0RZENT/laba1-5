list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 90]

common_elements = sorted(set(list1) & set(list2))

print("Общие элементы в порядке возрастания:", common_elements)