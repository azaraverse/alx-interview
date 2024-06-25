#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Constructs a pascal's triangle upto specified row count.
    """
    if n <= 0:
        return []

    # initialise the triangle with first number, 1
    triangle = [[1]]
    # loop through rows from index 1 (not 0) to nth index.
    for row_idx in range(1, n):
        # create subsequent rows, initialising them with 1
        new_row = [1]
        # loop through columns from index 1 (not 0)
        # range depends on row size (n)
        for col_idx in range(1, row_idx):
            # calculate the sum of each left and right index
            left_index = triangle[row_idx-1][col_idx-1]
            right_index = triangle[row_idx-1][col_idx]
            new_row.append(left_index + right_index)
        # append 1 to the end of iteration
        new_row.append(1)
        # append new row to the existing triangle and return
        # two for loops above to continue the loop
        triangle.append(new_row)
    # return the Pascal's Triangle
    return triangle
