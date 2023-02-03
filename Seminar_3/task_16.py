# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[0..N-1]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A[i]. Последняя строка содержит
# число X

# 5
# 1 2 3 4 5
# 3
# -> 1
counter = 0
A = list()
N = int(input("Input number N: "))

for i in range(N):
    A.append(int(input(f"Input A[{i}]: ")))
print(A)

X = int(input("Input number to find: "))

for i in range(len(A)):
    if A[i] == X:
        counter += 1

print(counter)