import numpy as np


def slice_me(family, start: int, end: int) -> list:
    """
    function that takes as parameters a 2D array,
    prints its shape, and returns a truncated version
    of the array based on the provided start and end arguments.
    """

    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("start and end must be integers")

    if start < 0 or end < 0:
        raise ValueError("start and end must be positive integers")

    if not all(isinstance(x, (int, float)) for row in family for x in row):
        raise ValueError("all list elements must be numbers")

    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("all lists are not the same size")

    arr = np.array(family)
    print("My shape is:", arr.shape)

    arr = arr[start:end, :]
    print("My new shape is:", arr.shape)

    fam = arr.tolist()
    return fam
