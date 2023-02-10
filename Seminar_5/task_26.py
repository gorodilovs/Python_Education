# Задача 26: Напишите программу, которая на вход принимает два числа
#  A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Input A: "))
b = int(input("Input B: "))

def recur(a1, b1):
    if b1 == 1:
        return a1
    if b1 != 0:
        return a1 * recur(a1, (b1-1))
print(recur(a, b))
