# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

plusSeqCounter = 0
plusSeqTemporary = 0

days = int(input("Input number of days from 1 to 100: "))
daysList = [0] * days

# Filling array with ranodms
for i in range(days):
    daysList[i] = random.randint(-50, 51)
    print(f"Day: {i}, Temp: {daysList[i]}")

# Seraching for plus degree sequences
for i in range(days):
    if daysList[i] >= 0:
        plusSeqTemporary += 1
    else:
        if plusSeqTemporary > plusSeqCounter:
            plusSeqCounter = plusSeqTemporary
        plusSeqTemporary = 0
print(f"Longest plus is: {plusSeqCounter} days!")