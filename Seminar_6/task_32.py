# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума)

list_1 = [6, 5, 3, 42, 53, 64, 7, 8, 9, 10, 5]
min = 4
max = 8
list_2 = list()

for i in range(len(list_1)):
    if (list_1[i] <= max and list_1[i] >= min):
        list_2.append(i)
print("Matched indexes:")
print(list_2)