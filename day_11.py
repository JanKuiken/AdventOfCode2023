"""
Advent Of Code 2023 --- Day 11: Cosmic Expansion ---
"""

import aoc_lib as aoc
from copy import deepcopy

# parse the input
# matrix = aoc.matrix_from_file('example_input_11.txt')
matrix = aoc.matrix_from_file('input_11.txt')

#aoc.print_matrix(matrix)
n_rows = len(matrix)
n_cols = len(matrix[0])

# expand the universe...
empty_rows = []
for row in range(n_rows):
    if all([matrix[row][col] == '.' for col in range(n_cols)]):
        empty_rows.append(row)
empty_cols = []
for col in range(n_cols):
    if all([matrix[row][col] == '.' for row in range(n_rows)]):
        empty_cols.append(col)

# nwhaaaw, we don't change the matrix,....
# we'll find the galaxies first and than....
galaxies = []
for row in range(n_rows):
    for col in range(n_cols):
        if matrix[row][col] == '#':
            galaxies.append([row,col])

print(empty_rows)
print(empty_cols)
print(galaxies, len(galaxies))

# for function expand_galaxies it is important to start from the end... 
empty_rows.reverse()
empty_cols.reverse()

def expand_galaxies(in_galaxies, amount):
    ret_val = deepcopy(in_galaxies) # we do not want to change the original (for part 2)
    for empty_row in empty_rows:
        temp = []
        for row, col in ret_val:
            if row > empty_row:
                row += amount
            temp.append([row,col])
        ret_val = temp
    for empty_col in empty_cols:
        temp = []
        for row, col in ret_val:
            if col > empty_col:
                col += amount
            temp.append([row,col])
        ret_val = temp
    return ret_val

# calculate 'manhatan' distances
def calc_total_distances(in_galaxies):
    total_distance = 0
    for row_1, col_1 in in_galaxies:
        for row_2, col_2 in in_galaxies:
            total_distance += abs(row_2 - row_1) + abs(col_2 - col_1)
    return total_distance

print('Solution part 1:', calc_total_distances(expand_galaxies(galaxies, 1)) // 2 )

# F*&k, close reading, not adding rows/cols, but replacing...., hence -1 in line below
print('Solution part 2:', calc_total_distances(expand_galaxies(galaxies, 1000000-1)) // 2 )


