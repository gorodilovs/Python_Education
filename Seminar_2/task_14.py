# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Input n: "))
power = 0
counter = 0

while power < n:   
    power = 2**counter
    counter += 1
    if power < n:
        print(power)