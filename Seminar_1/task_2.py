# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Input number: "))
sum = (number % 10) + ((number//10) % 10) + (number//100)
print(f"Result is: {sum}")