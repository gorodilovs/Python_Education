def sumnumbers(n, y = "Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

a = sumnumbers(5, "Pet")
print(a)

# * - variuos quantity of args
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 't'))
print(sum_str('q', 'w', 'e', 'r'))