"""
ISA Altitude Analysis
Version: 1.0.0
Author(s): Alijah McDonald, Eric Yoerg

Description: This file imports generated barometric pressure data from a .csv file
and plots ISA altitude based on a pressure --> ISA Altitude conversion.
"""

from turtle import end_fill
import numpy as np
from matplotlib import pyplot as plt 
import pandas as pd
from pandas import DataFrame
import os
import csv

def ISA_altitude():
    #define csv path to pull csv from
    csv_path = input('Please input the csv file path you would like to read:') 
    
    #import csv file
    #modify to input a single numpy array
    with open(csv_path, mode='r') as csv_file:
        #read csv that has specified input path
        df = pd.read_csv(csv_path)

        #create matrices of time and pressure values
        time, pressure = df["time"], df["pressure"]

    T_o = 518.4 #Mean sea level temperature rankine
    B = 0.00357 #lapse rate
    P_o = 101325 #Mean Sea level pressure

    #Convert pressure to pressure altitude and store inside altitude
    for x in range(len(pressure)):
        pressure[x] = ((T_o/B)*(1-((int(pressure[x])/P_o)**0.1903)))*0.3048

    print(pressure)
    #Write pressure altitude and time data to csv
    #change the file to pandas writer and make it so that the path is editable
    with open('C:\Ground-Station\post_flight_analysis\proc_data\Altitude.csv',mode='w') as alt_csv:
        
        #Create the csv writer
        writer = csv.writer(alt_csv)

        #Write time and pressure altitude
        writer.writerows(time)
        writer.writerows(pressure)


    #plt.plot(time,altitude)
    #plt.show()