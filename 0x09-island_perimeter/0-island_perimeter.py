#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of a rectangle by accesing
    avaialble 1s and using these to solve for the perimeter value.

    Perimeter = 2 * (l + w).

    Args:
        grid (list of list of int): Rectangle to calculate perimeter of.

    Returns:
        Perimeter value.
    """

    # grid = [
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 1, 0, 0, 0, 0],
    #   [0, 1, 0, 0, 0, 0],
    #   [0, 1, 1, 1, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    # ]

    # row helps to access each array/list
    # col helps to access each element in each list/array

    # row = grid[2] should print [0, 1, 0, 0, 0, 0]
    # col = row[1] should print 1
    # print(row)
    # print(col)

    grid_length = len(grid)
    width = 0
    length = 0

    for row in range(grid_length):
        for col in range(len(grid[row])):
            up = grid[row - 1][col]
            # down = (row + 1, col)
            left = grid[row][col - 1]
            # right = (row, col + 1)
            if grid[row][col] == 1:
                if row > 0 and up == 1:
                    width += 1
                if col > 0 and left == 1:
                    length += 1

    width += 1
    length += 1

    return 2 * (width + length)
