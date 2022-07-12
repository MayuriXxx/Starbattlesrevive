import numpy as np
import itertools
import time


class StarConstructor:
    def __init__(self, size=10, star_count=1):
        self.size = size
        self.star_positions = []
        self.star_count = star_count
        # all neighbour calculations except [0, 0]
        self.neighbours_calc = np.array([[i, j] for i, j in itertools.product(range(-1, 2), range(-1, 2)) if not(i==j==0)])

    def create_all_fields(self):
        # loop through all columns, to get all possibilities
        for column in range(0, self.size):
            self.construct_field(np.array([]), np.array([0, column], dtype=np.uint8))
        self.star_positions = np.unique(np.array(self.star_positions), axis=0)
        return self.star_positions

    def construct_field(self, star_coordinates, next_star, row=1, num_solutions=2):
        '''
            recursive function: create a recursive tree, where each 0 in the z matrix will be changed into a star.
            The star is marked as a 1. and written down in the stars. matrix.
            to limit the possibilities of the possible stars, each row and column and the neighbours, will be marked,
            when a star is set. we will loop through the remaining zeros.
            We will not loop through all zeros on the field, but the zero in the next row.
        :return condition: if isValid == True. ==> append to the solution
                if no zeros in the next row anymore ==> return for next row
        '''
        # Check condition of how many boards we want to generate
        if len(self.star_positions) == num_solutions:
            return True
        # get board from previous star
        stars = list(star_coordinates)
        stars.append(list(next_star))
        stars = np.array(stars)
        x = self.starposition_to_board(stars)
        if self.isValid(x):
            print(f"\n{ '=' *10}[ HERE is a valid board ]{'=' * 10}\n{x}\n\n")
            self.star_positions.append(stars)
            return True

        # look for the next possible star, by calculating the conditions
        y = np.ones(x.shape)
        z1 = np.dot(x, y)
        z2 = np.dot(x.T, y).T
        z = z1 + z2
        for star in stars:
            neighbours = np.array([star + elm for elm in self.neighbours_calc if self.size > (star+elm)[0] >= 0 and self.size > (star + elm)[1] >= 0])
            for neighbour in neighbours:
                z[neighbour[0]][neighbour[1]] += 1

        # select the next possible star
        zeros = np.array(np.where(z[row] == 0), dtype=np.uint8).T        # possible stars
        # print(f"z:\n{z}\nget zeros: {zeros}")
        curr_row = np.full(
                  shape=(zeros.shape[0], 1),
                  fill_value=row,
                  dtype=np.int
                )
        zeros = np.concatenate((curr_row, zeros), axis=1)       # only get the zeros, which is in the next row

        if len(zeros) == 0:             # there are no possibilities left
            return False

        for possible_star in zeros:
            e = self.construct_field(stars, next_star=possible_star, row=row+1)
        return False

    def starposition_to_board(self, positions):
        x = np.zeros((self.size, self.size), dtype=np.uint8)
        for point in positions:
            x[point[0]][point[1]] = 1
        return x

    # ================================[ Validate the input or field, that is constructed ]=============================
    def isValid(self, State):
        '''x = np.array([[0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [1, 0, 0, 0],
                      [0, 0, 1, 0]])'''
        x = np.array(State, dtype=np.uint8)
        '''print(f"first condition (each row and col can only have one star): {self.first_condition(x)}")
        print(f"second condition (each star cannot be next to another one): {self.second_condition(x)}")
        print(f"third condition (each field can only contain {self.star_count} of stars): {self.third_condition(x, x)}")'''
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


init_time = time.time()
Star = StarConstructor(size=9)
# Star.isValid(0)
possibilites = Star.create_all_fields()
print(time.time() - init_time)


