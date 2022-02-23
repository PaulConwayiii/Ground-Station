"""
TODO: Docstring
"""
<<<<<<< HEAD


def stitch(time, low, high, threshold):
=======
import numpy as np
def stitch(time,low,high,threshold):
>>>>>>> development
    """
    Inputs:
        time .................. numpy array [x]
        low ................... numpy array [[y_1],[y_2],[y_3]]
        high .................. numpy array [[y_1],[y_2],[y_3]]
        threshold ............. float value where low values will be replaced
        dim (opt, defalt=3) ... number of dependant variables (y-values)
    Returns:
        numpy array [[y_1],[y_2],[y_3]]
    Raises:
        None
    """
    # 1x3
    # row x col
    # n x 1
    stitch_arr = np.zeros((len(time),1))
    
    for xyz in range(3):
        for index in low:
            if(low[xyz[index]]>=threshold):
                stitch_arr[xyz[index]]=high[xyz[index]]
            else:
                stitch_arr[xyz[index]]=low[xyz[index]]
    return stitch_arr