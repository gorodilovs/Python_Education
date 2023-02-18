# Copy function to new variable name with same ref to memory
print("Copy name:")
def f(x):
    return x * x
a = f
print (a(5))


# Create function with input values of(function, int)
print("Func in func:")
def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calc2, 5, 45)

# Lambda func
print("Lambda:")
calc3 = lambda a,b: a + b
math(calc3, 5, 45)


# MAP - applied func to each
list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# FILTER - select each accordig to func
data = [1, 25, 3, 5, 8, 15, 235, 385]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)