import numpy as np

#xleh buat nama file   'types.py'    clash dgn library numpy

#all 0s matrix
print(np.zeros((2,3)))


# random integer value
print(np.random.randint(-4,8, size=(3,3)))
print("")

# the identity matrix
print(np.identity(5))
print("")


# be careful when copying arrays
arr = np.array([1,2,3])
brr = arr.copy()
brr[0] = 100

print(arr)


