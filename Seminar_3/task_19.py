# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

for i in range(k):
    temp = list_1[-1]
    for j in range(1, len(list_1)):
        list_1[-j] = list_1[-(j+1)]
    list_1[0] = temp
print(list_1)
