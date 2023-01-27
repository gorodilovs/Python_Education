n = int(input('Input n (kM per day): '))
m = int(input('Input m (total distance in kM): '))

import math
print(f"We need {math.ceil(m/n)} day(s) to our journey")