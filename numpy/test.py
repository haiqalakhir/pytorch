import numpy as np
 
a = np.array([1, 2, 3])
# print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

#get dimension
print(a.ndim)

#get shape
print(a.shape)

#get type
print(a.dtype)

#get size
print(a.itemsize)
print(f"b is {(b.itemsize)}")

#get total size
print(a.nbytes)
