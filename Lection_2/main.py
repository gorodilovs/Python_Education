list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]

# print in []
print(list_1) 
# print raw list
print(*list_1) 

for i in list_1:
    print(i)

# lenght
print(len(list_1)) 
# print element number
print(list_1[1]) 

# append - add elment to list
list_1.append(8)
print(list_1)

for i in range(5):
    list_1.append(i)
    print(list_1)

# pop(x) - delete last element, x - index

# !!! Keep in mind that in print func - ref to object 
# !!! so object will be changed even in print func

print(list_1.pop()) # 4  
print(list_1)
print(list_1.pop()) # 3
print(list_1)

# EVEN in variable declaration array will be changed
a = list_1.pop(1) # 1 - index of element to delete


# insert(x, y) - add element, x - index, y - value
print(list_1.insert(2, -11)) # none???
print(list_1)

print()

# TUPLES

t = ()
print(type(t))

t = (1, 5)
print(type(t))

# list
v = [1, 8, 9]
print(v)
print(type(v))

# list to tuple
v = tuple(v)
print(v)
print(type(v))


# multiple declaration
# only if number of variables equial number of elements in tuple
a, b, c = v
print(a, b, c)

for i in range(len(v)):
    print(v[i])

# Dictionaries

d = {}
d = dict()

# Add KEY - VALUE
d['q'] = 'qwerty'
print(d)

d['w'] = 'wertyu'
print(d)

d['e'] = 'ertyu'
d['r'] = 'rtyu'

# serchig by key
print(d['q'])

# delete element by key value
del d['w']
print(d)

# print keys
for item in d:
    print(item)

print()
# print key - value
for item in d:
    print("{}: {}".format(item, d[item]))

print()
# or 2 elemets for item
for (k, v) in d.items():
    print(k, v)
print()



# SET or FROZENSET

# contains only unique values
colors = {'red', 'green', 'blue'}
colors.add('red') # nothing happens, red already exists in colors
print(colors)

colors.add('grey')
print(colors) # grey - unique, added to set

# delete
colors.remove('red') # revove only if it exists, if not - exception
print(colors)

colors.discard('blue') # check if it in a set, if it is - delete it
print(colors)

# clear - delete all elements in set
colors.clear()
print(colors)


# Operations with SETs
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

# - copy set
c = a.copy()
# c = {1, 2, 3, 5, 8}
print(c)

# - union, new set with all unique values from two sets
u = a.union(b)
# u = {1, 2, 3, 5, 8, 13, 21}
print(u)

# - intersection, same elements from two sets
i = a.intersection(b)
# i = {2, 5, 8}
print(i)

# x.difference(y) - unique values from x compare to y
dl = a.difference(b)
# dl = {1, 3}
print(dl)

dr = b.difference(a)
# dr = {13, 21}
print(dr)

# complex functions allowed
q = a.union(b).difference(a.intersection(b))



# FROZENSET
a = {1, 8, 6}

# frozenset = const
b = frozenset(a)
print(b)