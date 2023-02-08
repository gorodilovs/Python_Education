import module_1

print(module_1.max1(5, 9))

# Import only one function
from module_1 import max1

# * - all functions form module
from module_1 import *

# Rename module to import
import module_1 as m1


# Recursion
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# Quick sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    lesser = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

print(quick_sort([14, 5, 2, 3 ,4, 34, 12, 42, 213,4, 2, 4 ]))
print(quick_sort([10, 5, 2]))

# Merge sort
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_2 = [1, 2, 3, 4, 2, 3, 1, 3, 6, 3, 12]
merge_sort(list_2)
print(list_2)
