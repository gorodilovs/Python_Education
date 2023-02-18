# FILTER - select each accordig to func
data = [1, 25, 3, 5, 8, 15, 235, 385]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)