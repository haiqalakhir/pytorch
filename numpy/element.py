import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)

#shape
print(f"shape = {(a.shape)}")

#get specific element [row, column]   # 0 index count
print(f"element = {(a[1, 5])}")

#get specific element [row, column]   # 0 index count  # start belakang
print(f"element = {(a[1, -2])}")

#get specific row
print(f"row = {(a[0, :])}")

#get specific column
print(f"column = {(a[:, 2])}")


#getting a little more fancy [startindex:endindex:stepsize]
print(f"slice = {(a[0, 1:6:2])}")

#change element
a[1,5] = 20
print(a)


#change row element
a[:,2] = 5
print(a)

#3d example
b = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
print(b)
print("")

#get specific element (work outside in)
print(f"3D = {(b[0,1,1])}")

#replace
print(f"replace = {(b[:,1,:])}")