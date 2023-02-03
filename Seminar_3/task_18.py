# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i].
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

A = list()
N = int(input("Input number of elements in the array: "))

for i in range(N):
    A.append(int(input(f"Input A[{i}]: ")))
print(A)

X = int(input("Input number to find: "))

closest = A[0]

# First closest
for i in range(len(A)):
    if abs(A[i] - X) < abs(closest - X):
        closest = A[i]
print(f"Closest is: {closest}")
