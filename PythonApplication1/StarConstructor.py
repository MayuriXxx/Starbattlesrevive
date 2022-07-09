import numpy as np
import itertools


class StarConstructor:
    def __init__(self, size=10, star_count=1):
        self.board = np.zeros((size, size))
        self.islands = np.zeros((size, size))
        self.strc = np.zeros((size, size))
        self.star_count = star_count
        # all neighbour calculations except [0, 0]
        self.neighbours_calc = np.array([[i, j] for i, j in itertools.product(range(-1, 2), range(-1, 2)) if not(i==j==0)])

    def construct_field(self):
        stars = np.array([[1, 1]])
        x = np.array([[0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0]])
        y = np.ones(x.shape)
        z1 = np.dot(x, y)
        z2 = np.dot(x.T, y).T
        z = z1 + z2
        for star in stars:
            neighbours = np.array([star + elm for elm in self.neighbours_calc])
            for neighbour in neighbours:
                z[neighbour[0]][neighbour[1]] += 1

        zeros = np.array(np.where(z == 0)).T
        print(f"z: {z}\nget zeros: {1}")

    # ================================[ Validate the input or field, that is constructed ]=============================
    def isValid(self, State):
        x = np.array([[0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [1, 0, 0, 0],
                      [0, 0, 1, 0]])
        print(f"first condition (each row and col can only have one star): {self.first_condition(x)}")
        print(f"second condition (each star cannot be next to another one): {self.second_condition(x)}")
        print(f"third condition (each field can only contain {self.star_count} of stars): {self.third_condition(x, x)}")
        if self.first_condition(x) and self.second_condition(x):
            return True
        return False

    def first_condition(self, state):
        # check Rows and columns
        x = np.array(state)
        y = np.ones((x.shape[0], 1))
        rows = np.dot(x, y)
        cols = np.dot(x.T, y)
        if max(rows) == min(rows) == self.star_count and max(cols) == min(cols) == self.star_count:
            return True
        return False

    def second_condition(self, state):
        # check if the stars are next to another star
        collisions = []
        index = np.array(np.where(state == 1)).T      # index = [[row, cols], ...]

        # get surrounding numbers and add them up
        for point in index:
            # get neighbour points and check if those neighbours are in the points
            neighbours = np.array([point + elm for elm in self.neighbours_calc])
            for possible_collision in neighbours:
                # if performance is important, then just return after at least one is found

                temp = np.array(np.where(possible_collision == index)).T
                if temp.shape[0] == 2:
                    if temp[0][0] == temp[1][0]:    # if they points found share the same row
                        return False
        return True

    def third_condition(self, state, field):
        # Check if our island only contains the number of starts we want
        return True


