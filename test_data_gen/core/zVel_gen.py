"""
Z Velocity Generator
Version: 1.0.1
Author(s): Jackson Sackrider

Description: This file generates a collection of velocity values for the z-axis based off the parameters 
contained in a JSON file.
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import os

def test_data():
    col_list = ["z_pos", "time"]
    csv_name = 'test_demo.csv'
    TestData = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), usecols=col_list)
    time, z_pos = TestData["time"], TestData["z_pos"]
    pd.set_option('max_row', None)
    Velocity(z_pos, time)

def Velocity(z_pos, time):
    for n in range(0, np.size(time)):
        delta_t = time[n+1] - time[n]
        z_velocity = (z_pos[n + 1] - z_pos[n]) / delta_t
        print(z_velocity)
        n += 1
        
    
    

test_data()

"""
Code Review
Author: Paul Conway

1. Line 24: n in range(value) will default start at 0 unless a different augument is passed
You can remove the redundant 0
ie: "n in range(value)" does the same as "n in range(0, value)"

2. Line 24: You are setting the max value too high
size will report the number of items in a list
ie:
list = ['a', 'b', 'c']
np.size(list) will evaluate to 3, but the maxinum index for the list is 2
Change "range(np.size(time))" to "range(np.size(time) - 1)"
This will remove the error at the end
However, this will result in you having one less data point for velocity than position
To fix this, you can just can just insert a point at the start equal to the first value you calculated
ie: velocity = ['a','b','c']
velocity would become: ['a','a','b','c']

3. Line 28: n automatically indexes
n is overwritten each loop, so this line doesn't even change n once you iterate into a new loop
You can remove this line completely

4. This is only calculating z velocity. Should be calculating x and y velocity as well
I assume you were waiting to add that until you could make sure z velocity was working properly 

5. Results should be stored in the csv file with appropriate header names


Style notes (functional code, but unconventional):
1. Function names generally start with a lowercase letter and are verbs

"""
