#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of a rectangle by accesing
    avaialble 1s and using these to solve for the perimeter value.

    Assume each land cell (1) starts with contributing 4 to the perimeter,
    since it has four sides. If a land cell has a neighbour above it, it
    shares a side with that neighbour, so subtract 2 from the perimeter.
    If a land cell also has a neighbour to its left, it shares another
    side, so subtract 2 from the perimeter.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter value of the land.
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

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                up = grid[row - 1][col]
                left = grid[row][col - 1]

                perimeter += 4
                # check the top
                if row > 0 and up == 1:
                    perimeter -= 2
                # check the left
                if col > 0 and left == 1:
                    perimeter -= 2

    return perimeter
