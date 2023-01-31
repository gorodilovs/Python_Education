# Задача №15. 
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

n = int(input("Input number of watermelons: "))
waterList = [0] * n

for i in range(n):
    waterList[i] = random.randint(1, 10)
    print(waterList[i])

min = waterList[0]
max = waterList[0]

for i in range(n):
    if waterList[i] > max:
        max = waterList[i]
    if waterList[i] < min:
        min = waterList[i]
print(f"Max is {max}, min is {min}")