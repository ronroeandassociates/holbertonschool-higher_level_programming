#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascal’s triangle of n
    """


def pascal_triangle(n):
    """Returns lists """

    if n <= 0:
        return []

    result = []
    tmpList = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(tmpList[x] + tmpList[x - 1])
            tmpList = row
            result.append(row)
    return result
