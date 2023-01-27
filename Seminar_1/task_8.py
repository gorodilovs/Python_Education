# Задача 8: Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Примеры:
# Примечание: каждое считывание производится с новой строки
# 3 2 4 -> yes
# 3 2 1 -> no

dimensionN = int(input("Input N: "))
dimensionM = int(input("Input M: "))
areaToSplit = int(input("Input area to split: "))

if (areaToSplit < dimensionN * dimensionM and (areaToSplit % dimensionM == 0 or areaToSplit % dimensionN == 0)):
    print("Yes! We can split!")
else:
    print("No, we can't do it!")