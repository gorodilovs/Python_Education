year = int(input("Input year: "))


# leapyear = False
# if (year % 4 == 0 ):
#     leapyear = True
#     if (year % 100 == 0):
#         leapyear = False
#     if (year % 400 == 0):
#         leapyear = True

# if (leapyear):
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year!")


if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("This is a leap year!")
else:
    print("This is not a leap year!")