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
    csv_name = 'test_data.csv'
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

Line 10: You do not need matplotlib in this file.
This file should not be doing any plotting.
Plotting values will be handled in a different file.

Line 19: File paths should be system independant.
Your code there would not work on any other system without modifying the path.
Paths should never be hard coded.

line 25: delta for time should not be hard coded.
It should imported from the JSON file.
Remember that CSV files are generated locally, so the JSON file correlating to that CSV will always be present

line 25: Denominator has redudant terms
(time + delta) - time always evaluates to delta

Line 25: You are adding the time delta to position.
time has units of seconds, position has units of meters

Line 25: Here is what the formula should be:
Function notation (what you'll see in math class): V = (z(time + delta) - z(time))/ delta
How that looks in code: V = (z[t[n + 1]] - z[t[n]]) / (t[n + 1] - t[n])
where n is an index variable
Since t[n+1] - t[n] is a constant, we can label it delta and rewrite:
V = (z[t[n + 1]] - z[t[n]]) / delta
This will all have to be in a for loop that loops for the number of rows present


Changes made:
1. Commented out line 10
2. Added csv_name variable. For now this can be hard coded but this is at least system independant
3. Modified line 19 to be system independant
4. Added os import

Currently this will

Style notes (functional code, but unconventional)

Line 26: Parenthesis for function calls should not be separated from the function
"print('string')" is prefered over "print ('string')"

Line 16 and line 24: Function names generally begin with a lowercase letter and are verbs
"""
