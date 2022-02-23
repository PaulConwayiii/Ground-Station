"""
TODO: Docstring
"""
import numpy as np
def stitch(time,low,high,threshold):
    """
    Inputs:
        time .................. numpy array [x]
        low ................... numpy array [y_1,y_2,...,y_n]
        high .................. numpy array [y_1,y_2,...,y_n]
        threshold ............. float value where low values will be replaced
        dim (opt, defalt=3) ... number of dependant variables (y-values)
    Returns:
        numpy array [x,y_1,y_2,...,y_n]
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