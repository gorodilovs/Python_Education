
# print('Input first string:')
# a = int(input())
# b = int(input('Input second string:'))

# print(a,  ' + ', b, ' = ', a+b)



# округление числел
a = 5
b = 6

print(a**b)
print(round(a*b, 3))

# Сокращенное присваивание i++;
iter = 2
iter += 3
iter -= 4
iter *= 5
iter /= 4
iter //= 4 # Деление нацело
iter %= 5  # Остаток от деления
iter **= 5 # В степень

# Логические операции сравнения
a = 1 > 4  # Bool = false;
a = 1 < 4 and 5 > 2 # true + true
a = 1 == 2 # if (1 == 2) a = ture; else a = false;
a = 1 != 2 # true
a = 1 < 3 < 5 < 10 # true
a = 'qwe'
b = 'qwe'
print (a == b) # true

# Ветвления if - elif (else-if)
username = input('Input name: ')
if username == 'Masha':
    print('Wow, this is Masha!')
elif username == 'Marina':
    print('Congratulations, Marina!')
elif username == 'Ilnar':
    print('Ilnar - top!')
else:
    print('Hello, ', username)

# While
n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print (summa)


# While - else
i = 0
while i < 5:
    # if i == 3:
    #     break  - ## avoid (end of while) == else
    i += 1
else:
    print("End of while == else")
print (i) 

# for 
for i in 1, -2, 13, -4, 15:
    print (i)

# range()
r = range(5) # 0 1 2 3 4 
r = range(2, 5) # 2 3 4
r = range(0, -5) # ----
r = range(1, 10, 2) # 1 3 5 7 9
r = range(100, 0, -20) # 100 80 60 40 20

for i in r: # for i in range(100, 0 , -20)
    print(i)

# Strings
a = 'qwerty'
for i in a:
    print(i)

text = 'qwerYW OASjoias LAS kljdas ALSDU'
print(len(text)) # len == Length
print ('LAS' in text) ## bool 
print (text.lower())
print (text.upper())
print (text.replace('LAS', 'las'))

# Index in strings
text = 'qwerty'
print(text[0]) # q
print(text[1]) # w

print(text[len(text) - 1])  # y
print(text[-1]) # y

print(text[:]) # qwerty
print(text[:2]) # qw
print(text[2:]) # erty
print(text[2:4]) # er
print(text[2:-1]) # ert

print(text[0:len(text):2]) # qet [start:end:step]
print(text[::2]) # qet
