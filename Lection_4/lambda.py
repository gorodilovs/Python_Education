list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_res = list()

for item in range(len(list_1)):
    if (list_1[item] % 2 == 0):
        res = (list_1[item], list_1[item]*list_1[item])
        list_res.append(res)
print(list_res)


# Returns list where some fuction applyed for each element
def select(f, col): # == map()
    return [f(x) for x in col]

# Select elements by some function to new list
def where(f, col): # == filter
    return [x for x in col if f(x)]

list_2 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list_2)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
