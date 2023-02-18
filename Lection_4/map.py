# MAP - applied func to each

data = " 15 235 234 2 563 345 24 2345 34"
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)