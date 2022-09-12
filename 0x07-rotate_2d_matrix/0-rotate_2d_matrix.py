#!/usr/bin/python3
"""
defines a function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotates an n x n 2D matrix by
    90 degrees
    """
    length = len(matrix)
    list2 = []  # holds rotated list
    start = 0  # holds position
    for y in range(length):
        list1 = []
        for i in range(len(matrix)):
            list1.append(matrix[length - 1][start])
            length = length - 1
        list2.append(list1)
        length = len(matrix)
        start = start + 1
    for i in range(length):
        matrix[i] = list2[i]
