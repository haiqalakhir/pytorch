import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

print(before.shape)

after = before.reshape((4,2))
print(after)


# vertical stacking vector
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1, v2]))
# output
# [[1 2 3 4]
#  [5 6 7 8]]