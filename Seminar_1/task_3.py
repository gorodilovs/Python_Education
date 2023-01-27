class1 = int(input('Input number of students in the 1st class: '))
class2 = int(input('Input number of students in the 2nd class: '))
class3 = int(input('Input number of students in the 3rd class: '))

import math
print(f"We should buy {math.ceil(class1/2) + math.ceil(class2/2) + math.ceil(class3/2)} new tables for the math classes.")
