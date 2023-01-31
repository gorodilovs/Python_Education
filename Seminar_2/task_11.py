# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

fib1 = 0
fib2 = 1
counter = 2
answerFound = False

userInput = int(input("Input number: "))

while answerFound == False:
    fibCurr = fib1 + fib2
    fib1 = fib2
    fib2 = fibCurr
    counter += 1
    # print(f"Current fib: {fibCurr}")

    if userInput == fibCurr:
        print(f"Number is {counter} number Fibonacci!")
        answerFound = True
    if fibCurr > userInput:
        print("-1")
        answerFound = True

    