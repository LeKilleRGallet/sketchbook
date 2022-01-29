import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# b = np.array(a)
c=[_[:] for _ in a]

a[1][1] = 10

print(c)

print(a)