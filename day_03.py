"""
Advent Of Code 2023 --- Day 3: Gear Ratios ---
"""

import aoc_lib as aoc

from collections import namedtuple
from string import digits

matrix = aoc.matrix_from_file('input_03.txt')

aoc.print_matrix(matrix)

n_rows = len(matrix)
n_cols = len(matrix[0])
max_matrix_point = aoc.MatrixPoint(n_rows-1, n_cols-1)



# find the numbers...
Number = namedtuple("Number", "row, col, len, val")
numbers = []
for row in range(n_rows):
    reading_number = False
    start_col = None
    for col in range(n_cols):
        is_digit = matrix[row][col] in digits 
        if reading_number:
            if not is_digit:
                number_len = col - start_col
                val = int(''.join(matrix[row][start_col:col]))
                numbers.append(Number(row, start_col, number_len, val)) 
                reading_number = False
        else:
            if is_digit:
                start_col = col
                reading_number = True
    if reading_number:
        number_len = col + 1- start_col
        val = int(''.join(matrix[row][start_col:col+1]))
        numbers.append(Number(row, start_col, number_len, val))

neighbours_of_numbers = {}
for num in numbers:
    n = set()
    for i in range(num.len):
        neighbours = aoc.matrix_neighbours(aoc.MatrixPoint(num.row, num.col + i), max_matrix_point=max_matrix_point)
        n = n.union(neighbours)
    neighbours_of_numbers[num] = n

# part 1: filter to part numbers

NON_SYMBOLS = set(digits)
NON_SYMBOLS.add('.')
part_numbers = []
for num in numbers:
    neighbour_chars = set()
    for n in neighbours_of_numbers[num]:
        neighbour_chars.add(matrix[n.row][n.col])
    symbols = neighbour_chars.difference(NON_SYMBOLS)
    if len(symbols) > 0:
        part_numbers.append(num.val)

print('Solution part 1: ', sum(part_numbers))


# part 2: find gears

gear_ratios = []
for row in range(n_rows):
    for col in range(n_cols):
        if matrix[row][col] == '*':
            gear_matrix_point = aoc.MatrixPoint(row,col)
            gear_n_numbers = 0
            gear_ratio = 1
            for num, neighbours in neighbours_of_numbers.items():
                if gear_matrix_point in neighbours:
                    gear_n_numbers += 1
                    gear_ratio *= num.val
            if gear_n_numbers == 2:
                gear_ratios.append(gear_ratio)

print('Solution part 2: ', sum(gear_ratios))

