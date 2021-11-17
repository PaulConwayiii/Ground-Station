"""
Position Generator
Author(s): Maxwell Gorley

Description: This file generates a plot of acceleration over time from a CSV file.
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Generate_Plot(csv_name):
     def import_data(csv_name):
        #Define which files should be imported from the test data
        col_list = ["time","x_pos", "y_pos", "z_pos",'pressure', "x_velocity", "y_velocity", "z_velocity", "x_acceleration", "y_acceleration", "z_acceleration", "x_angle", "y_angle", "z_angle"]
        #Define the name of the test data csv and import it
        TestData = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), usecols=col_list)
        #Gather all the info from the columns
        time, x_pos, y_pos, z_pos, pressure, x_velocity, y_velocity, z_velocity, x_acceleration, y_acceleration, z_acceleration, x_angle, y_angle, z_angle = TestData["time"], TestData["x_pos"], TestData["y_pos"], TestData["x_pos"], TestData["pressure"], TestData["x_velocity"], TestData["y_velocity"], TestData["z_velocity"], TestData["x_acceleration"], TestData["y_acceleration"], TestData["z_acceleration"], TestData["x_angle"], TestData["y_angle"], TestData["z_angle"]
        #Call the function get_Angle
        draw_plot(time, x_acceleration, y_acceleration, z_acceleration)

def draw_plot(time, x_acceleration, y_acceleration, z_acceleration):
    plt.plot(time,x_acceleration)
    plt.plot(time,y_acceleration)
    plt.plot(time,z_acceleration)