import numpy as np

a = np.array([1,2,3,4])

print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print("")


b = np.array([1,0,1,0])

print(a + b)
print("")


#take the sin
print(np.cos(a))

#linear algebra

ave = np.ones((2,3))
print(ave)

blu = np.full((3,2), 2)
print(blu)


print(np.matmul(ave,blu))


# find determinant
c = np.identity(3)
print(np.linalg.det(c))

print("")
#statistic


stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats))
print(np.max(stats))