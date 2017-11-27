# Array-oriented programming with Arrays
# The objective is to calculate euclidian distance between all possible points in xs and ys

import numpy as np

points = np.arange(0, 1, 0.01)

xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()


xarr = np.arange(1.1, 1.6, 0.1)
yarr = np.arange(2.1, 2.6, 0.1)
cond = np.array([True, False, True, True, False])


# the following 2 are the same, but I actually want something else
result = [(x if c else y) for x in xarr for y in yarr for c in cond]

for i in range(5):
    for j in range(3):
        for k in range(4):
            print('i = {}, j = {}, k = {}\n'.format(i, j, k) + 20 * '-')

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# with np.where, things are much faster and concise.i

result_w = np.where(cond, xarr, yarr)

arr = np.random.randn(4, 4)

np.where(arr > 0, 2, -2)

# or we can combine scalars and arrays when using np.where

arr = np.random.randn(4, 4)

print(np.where(arr < 0, 2, arr))

# Mathematical and Statistical Methods

arr = np.arange(15).reshape(3, 5)


# lets compute the mean of each row.
# rows are axis = 0, but that will actually give us an array with means
# of each column.

print(arr.mean(axis=0))

# the trick is that when we tell numpy to calculate
# mean given axis=0, it looks at the array as combination of raws. if
# instead, we passed axis=1, it would look at it as a cominations of
# columns. The reason this is important is because numpy does everything
# element-wise. That is, if I need the mean of the raws and it functions
# element-wise, than I have to tell it too look at the array as a combi-
# nation of columns, which will enable it to operate element-wise upon
# columns and give me the desired outcome.

print(arr.mean(axis=1))

# Sorting

# sorting can be done in place with .sort() method.

arr = np.random.randn(6)
arr.sort()

# Multidimentional
arr = np.random.randn(5,3)

# if I want to sort across rows, I would pass the axis = 1

arr.sort(axis=1)

# Again, the same logic works, as before. We need to keep in mind
# the elementwise philosophy of NumPy.

# These methods are mutating. 
# The top level functions such as np.sort() are not mutating and
# returne a copy of the array


