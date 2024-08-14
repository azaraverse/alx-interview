#!/usr/bin/python3
""" Rotate 2D Matrix
"""
from typing import List, Any


def rotate_2d_matrix(matrix: List[List[Any]]):
    """ Rotate a matrix in place 90 degrees clockwise
    """
    n = len(matrix)

    # perform transposition on original matrix
    for i in range(n):
        for j in range(i, n):
            # move elements
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse transposed matrix
    for i in range(n):
        matrix[i].reverse()
