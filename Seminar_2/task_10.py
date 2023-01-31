# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random
tails = 0
heads = 0

n = int(input("Input number of coins: "))
coinList = [0] * n

for i in range(n):
    coinList[i] = random.randint(0, 1)

for i in range(n):
    if coinList[i] == 0:
        heads += 1
        print("Head: 1")
    else:
        tails += 1
        print("Tail 0")

if heads == tails:
    print(f"Draw. Min is {heads}")
elif heads > tails:
    print(f"Heads wins! You should swap tails. Min {tails}")
else:
    print(f"Tails wins! You should swap heads. Min {heads}")
