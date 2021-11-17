"""
Author: Paul Conway

Opening CSV, demonstrating int
"""

import os  # For file operations
import pandas as pd  # For dataframe operations
import numpy as np  # For math operations
import matplotlib.pyplot as plt  # For plotting
import integrate as nint # Numerical integration

selection = input("Do you wish to plot test data? (y/n)")
if selection.lower() == 'y':
    selection = input("Input the name of a test data file (without extension):")
    path_name = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "test_data_gen",
            "local_data",
            "generated",
            selection + ".csv",
        )
    )
    if os.path.exists(path_name):
        col_list = [
            "z_pos",
            "y_pos",
            "x_pos",
            'pressure',
            "z_velocity",
            "y_velocity",
            "x_velocity",
            "z_acceleration",
            "y_acceleration",
            "x_acceleration",
            'time',
        ]
        file_data = pd.read_csv(path_name, usecols=col_list)
        
        alt_plot = plt.plot(file_data["time"], nint.left_sum(file_data["time"],file_data["z_pos"]))
        plt.show()

    else:
        print("That file does not exists (" + selection + ".csv)")
else:
    pass
