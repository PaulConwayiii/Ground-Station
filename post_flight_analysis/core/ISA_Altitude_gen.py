"""
ISA Altitude Analysis
Version: 1.0.0
Author(s): Alijah McDonald

Description: This file imports generated barometric pressure data from a .csv file
and plots ISA altitude based on a pressure --> ISA Altitude conversion.
"""

import numpy as np
from matplotlib import pyplot as plt 
import pandas as pd
from pandas import DataFrame
import os

#define csv path to pull csv from
csv_path = input('Please input the csv file path you would like to read:') 

#import csv file
with open(csv_path, mode='r') as csv_file:
    #read csv that has specified input path
    df = pd.read_csv(csv_path)

    #create matrices of time and pressure values
    time, pressure = df["time"], df["pressure"]

    #print values
    print(str(time))
    print(str(pressure))

altitude = []

for x in pressure:
    altitude(x) = pressure(x)

plt.plot(time,altitude)
plt.show()