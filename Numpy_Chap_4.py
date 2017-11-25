# Array-oriented programming with Arrays
# The objective is to calculate euclidian distance between all possible points in xs and ys

import numpy as np

points = np.arange(0, 1, 0.01)

xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()


xarr = np.arange(1.1,1.6,0.1)
yarr = np.arange(2.1,2.6,0.1)
cond = np.array([True,False,True,True,False])


# the following 2 are the same, but I actually want something else
result = [(x if c else y) for x in xarr for y in yarr for c in cond]

for i in range(5):
    for j in range(3):
        for k in range(4):
            print('i = {}, j = {}, k = {}\n'.format(i,j,k) + 20*'-')

result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
# with np.where, things are much faster and concise.i

result_w = np.where(cond,xarr,yarr)

arr = np.random.randn(4,4)

np.where(arr>0,2,-2)

# or we can combine scalars and arrays when using np.where

arr = np.random.randn(4,4)

print(np.where(arr<0, 2, arr))
