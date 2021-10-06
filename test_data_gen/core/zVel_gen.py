"""
Z Velocity Generator
Version: 1.0.0
Author(s): Jackson Sackrider

Description: This file generates a collection of velocity values for the z-axis based off the parameters 
contained in a JSON file.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame

def test_data():
    col_list = ["z_pos", "time"]
    TestData = pd.read_csv("C:/Users/Jackson L Sackrider/Documents/Ground Station, Epic!/Ground-Station/test_data_gen/local_data/generated/test_data.csv", usecols=col_list)
    time, z_pos = TestData["time"], TestData["z_pos"]
    pd.set_option('max_row', None)
    Velocity(z_pos, time)

def Velocity(z_pos, time):
    z_velocity = ((z_pos + 0.01) - z_pos)/((time + 0.01) - time)
    print (z_velocity)
    

test_data()