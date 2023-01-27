numberInRow = int(input("Input number of the car of the train in the row: "))
numberId = int(input("Input unique number of the car of the train: "))

if (numberInRow < numberId):
    print(f"Total number of cars in the train is {numberInRow + numberId -1}")
else:
    print("We havn't enough data.")
