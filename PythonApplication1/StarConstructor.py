import numpy as np
import itertools

class StarConstructor:
    def __init__(self, size=10, starcount=1):
        self.board = np.zeros((size, size))
        self.islands = np.zeros((size, size))
        self.strc = np.zeros((size, size))

    def isValid(self, State):
        x = np.array([[0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [1, 0, 0, 0],
                      [0, 0, 0, 1]])
        print(self.first_condition(x))
        print(self.second_condition(x))

    def first_condition(self, state):
        # check Rows and columns
        x = np.array(state)
        y = np.ones((x.shape[0], 1))
        rows = np.dot(x, y)
        cols = np.dot(x.T, y)
        if max(rows) == min(rows) == 1 and max(cols) == min(cols) == 1:
            return True
        return False

    def second_condition(self, state):
        # check if there are any neighbours
        collisions = []
        index = np.array(np.where(state == 1)).T      # index = [[row, cols], ...]
        neighbours_calc = np.array([[i, j] for i, j in itertools.product(range(-1, 2), range(-1, 2))])
        # get surrounding numbers and add them up
        for point in index:
            # get neighbour points and check if those points are in the points
            neighbours = np.array([point + elm for elm in neighbours_calc])
            collisions.append(np.array_equal(neighbours, index))

        return collisions


