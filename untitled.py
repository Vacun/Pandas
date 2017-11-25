import numpy as np

d = {i: np.random.rand() for i in range(7)}

print(d)


total = 0
for i in [1, 2, None, 5, None, 4]:
    if i == None:
        continue
    total += i

sequence = [1, 3, 4, 0, 2, 5, 7, 12]

total_till_5 = 0
for i in sequence:
    if i == 5:
        break
    total_till_5 += i
