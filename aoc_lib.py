"""
Some functions that are multiple times used in AoC 2023
"""

import pprint
from collections import namedtuple


def lines_from_file(file_name):
    """
    Returns a list of lines (with trailing \n removed)
    """
    with open(file_name) as f:
        lines = f.readlines()
        lines = [l.removesuffix('\n') for l in lines]
        return lines

def matrix_from_file(file_name):
    """
    Returns a list (rows) of lists (cols) of chars from a file
    """
    lines = lines_from_file(file_name)
    return [ [ c for c in line ] for line in lines ]

pp = pprint.PrettyPrinter(indent=4, width=120)

def pprint(stuff):
    pp.pprint(stuff)

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end='')
        print('\n', end='')

# some named tuples
Point = namedtuple("Point", "x y")
MatrixPoint = namedtuple("MatrixPoint", "row col")


def neighbours(x, y, xmin=0, xmax=100, ymin=0, ymax=100):
    """
    Returns a set of (x,y) tuples
    """
    retval = set()
    for the_x in range(x-1, x+2):
        for the_y in range(y-1, y+2):
            if (     the_x >= xmin
                 and the_x <= xmax
                 and the_y >= ymin
                 and the_y <= ymax ) :
                retval.add((the_x, the_y))
    retval.remove((x,y))
    return retval

def point_neighbours(point, 
                     min_point=Point(0,0), 
                     max_point=Point(100,100)):
                    
    results = neighbours(point.x, 
                         point.y,
                         xmin = min_point.x,
                         xmax = max_point.x,
                         ymin = min_point.y,
                         ymax = max_point.y )

    return set([Point(res[0], res[1]) for res in results])

def matrix_neighbours(matrix_point, 
                      min_matrix_point=MatrixPoint(0,0),
                      max_matrix_point=MatrixPoint(100,100)):
                      
    results = neighbours(matrix_point.row, 
                         matrix_point.col,
                         xmin = min_matrix_point.row,
                         xmax = max_matrix_point.col,
                         ymin = min_matrix_point.row,
                         ymax = max_matrix_point.col )

    return set([MatrixPoint(res[0], res[1]) for res in results])
