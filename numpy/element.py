import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# print(a)

#shape
print(f"shape = {(a.shape)}")


#get specific element [row, column]   # 0 index count
print(f"shape = {(a[1, 5])}")

#get specific element [row, column]   # 0 index count  # start belakang
print(f"shape = {(a[1, -2])}")