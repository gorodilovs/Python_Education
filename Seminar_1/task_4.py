# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
# ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

S = int(input("Input total number: "))
serg = S/6
petr = S/6
kate = S - 2 * S/6
print(f"Kate: {kate}, Sergey: {serg}, Petr: {petr}")