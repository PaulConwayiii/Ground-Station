"""
Z Velocity Generator
Version: 1.0.2
Author(s): Jackson Sackrider

Description: This file generates a collection of velocity values for the z-axis based off the parameters 
contained in a JSON file.
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
import os
def test_data():
    col_list = ["z_pos", "y_pos", "x_pos", "time"]
    csv_name = 'test_data.csv'
    TestData = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), usecols=col_list)
    time, z_pos, y_pos, x_pos = TestData["time"], TestData["z_pos"], TestData["y_pos"], TestData["x_pos"]
    pd.set_option('max_row', None)
    get_Velocity(z_pos, time, y_pos, x_pos, csv_name)


def get_Velocity(z_pos, time, y_pos, x_pos, csv_name):
        df = pd.DataFrame(columns=["x_velocity", "y_velocity", "z_velocity"])
        for n in range(0, np.size(time) - 1):
            delta_t = time[n+1] - time[n]
            z_velocity = (z_pos[n + 1] - z_pos[n]) / delta_t
            x_velocity = (x_pos[n + 1] - x_pos[n]) / delta_t
            y_velocity = (y_pos[n + 1] - y_pos[n]) / delta_t
            df = df.append(pd.Series([x_velocity, y_velocity, z_velocity], index=df.columns), ignore_index = True)
        df.to_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), index=False)




        
    
    

test_data()
