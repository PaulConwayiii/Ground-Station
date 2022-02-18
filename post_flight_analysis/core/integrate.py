"""
Author: Paul Conway

Performs various numeric integrations

TODO: Finish this dosstring
"""
import numpy as np

def left_sum(num_input):
    """
    Inputs:
        x, list-like type
        y, list-like type
    Return:
        list type
    Raises:
        IndexError if x and y have different sizes
    """
    x = num_input[:,0]
    y = num_input[:,1]

    col_width = len(num_input)
    row_width = len(num_input[0])
    num_output = np.zeros([col_width,row_width])
    # TODO: dont require list type
    #if type(x) != 'list':
    #    x = list(x)
   # if type(y) != 'list':
       # y = list(y)

    if len(x) == len(y):
        num_sum = 0
        for n in range(1, row_width - 1):
            # Will handle changes in data timing
            delta = num_input[0,[n+1]] - num_input[0,[n]]
            
            num_sum = num_sum + (delta * num_input[1,[n]])
            print(str(num_sum))
            print(str(delta * num_input[0,[n]]))
            num_output[0,[n]] = n
            num_output[1,[n]]= num_sum
        return num_output
    else:
        raise IndexError("Array sizes must match")
