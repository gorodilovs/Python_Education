#  Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
#  вы расплачивались за проезд и получали билет с номером. Счастливым
#  билетом называют такой билет с шестизначным номером, где сумма первых
#  трех цифр равна сумме последних трех. Т.е. билет с номером
#  385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#  программу, которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input("Input ticket number: "))
leftPartSum = (ticketNumber//1000) % 10 + (ticketNumber//1000)//10 % 10 + (ticketNumber//1000)//100
print(f"Left part sum is: {leftPartSum}")
rightPartSum = (ticketNumber % 10) + (ticketNumber//10) % 10 + (ticketNumber//100) % 10
print(f"Rigth part sum: {rightPartSum}")
if (leftPartSum == rightPartSum):
    print("This is a lucky ticket!")
else:
    print("This is a common ticket.")