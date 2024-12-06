my_list = [10, 20, 30, 40, 50]

print("Элемент с индексом 2:", my_list[2])

my_list[1] = 25
print("После замены:", my_list)

my_list.append(60)
print("После добавления в конец:", my_list)

my_list.insert(3, 35)
print("После вставки на позицию 3:", my_list)

my_list.remove(40)
print("После удаления 40:", my_list)

del my_list[0]
print("После удаления первого элемента:", my_list)

print("Дублированный список:", my_list * 2)