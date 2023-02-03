# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
unique = set()

for i in list_1:
    unique.add(i)

print(f"Number of unique values in list is: {len(unique)}")