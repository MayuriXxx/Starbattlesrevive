import numpy as np
import matplotlib.pyplot as plt
import itertools

size = 4
neighbours_calc = np.array([[i, j] for i, j in itertools.product(range(-1, 2), range(-1, 2)) if not (i == j == 0)])
x = np.array([[1, 0, 0, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]])
y = np.ones(x.shape)
z1 = np.dot(x, y)
z2 = np.dot(x.T, y).T
z = z1 + z2
stars = np.array(np.where(x == 1)).T
for star in stars:
    neighbours = np.array([star + elm for elm in neighbours_calc if
                           size > (star + elm)[0] >= 0 and size > (star + elm)[1] >= 0])
    for neighbour in neighbours:
        z[neighbour[0]][neighbour[1]] = z[star[0]][star[1]]

    print(z)

zeros = np.array(np.where(z == 0)).T
print(f"z: {z}\nget zeros: {zeros.shape}")
