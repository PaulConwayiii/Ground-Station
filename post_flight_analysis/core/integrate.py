"""
Author: Paul Conway

Performs various numeric integrations

TODO: Finish this dosstring
"""


def left_sum(x, y):
    """
    Inputs:
        x, list-like type
        y, list-like type
    Return:
        list type
    Raises:
        IndexError if x and y have different sizes
    """

    # TODO: dont require list type
    if type(x) != 'list':
        x = list(x)
    if type(y) != 'list':
        y = list(y)

    if len(x) == len(y):
        num_sum = 0
        for n in range(len(x) - 1):
            # Will handle changes in data timing
            delta = x[n + 1] - x[n]
            num_sum = num_sum + (delta * y[n])
        return num_sum
    else:
        raise IndexError("Array sizes must match")
