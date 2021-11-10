"""
Angle Generator
Version: 1.0.0
Author(s): Maxwell Gorley

Description: This file generates a collection of angle values for the x, y, and z-axis based off the parameters
contained in a JSON file.
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
import os

def Generate_Angle(csv_name): 
    def import_data(csv_name):
        #Define which files should be imported from the test data
        col_list = ["z_pos", "y_pos", "x_pos",'pressure', "z_velocity", "y_velocity", "x_velocity", "z_acceleration", "y_acceleration", "x_acceleration", "time"]
        #Define the name of the test data csv and import it
        TestData = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), usecols=col_list)
        #Gather all the info from the columns
        time, z_pos, y_pos, x_pos, z_velocity, y_velocity, x_velocity = TestData["time"], TestData["z_pos"], TestData["y_pos"], TestData["x_pos"], TestData["z_velocity"], TestData["y_velocity"], TestData["x_velocity"]
        #Call the function get_Angle
        get_Angle(z_pos, time, y_pos, x_pos, z_velocity, y_velocity, x_velocity, TestData, csv_name)


    def get_Angle(z_pos, time, y_pos, x_pos, z_velocity, y_velocity, x_velocity, TestData, csv_name):
            #Initialize angle values
            x_angle=0
            y_angle=0
            z_angle=0
            #Create a new data frame with the to be calculated columns
            df = pd.DataFrame(columns=["x_angle", "y_angle", "z_angle"])
            #Loop for every amount of times there is a change in time (run as long as there is data)
            for n in range(0, np.size(time) - 1):
                #Find the difference in time (the delta of time)
                delta_t = time[n+1] - time[n]
                #Calculate the three angles
                if z_pos[n] > 0:
                    x_angle = ((((y_pos[n]*z_velocity[n])-(z_pos[n]*y_velocity[n]))/((x_pos[n]**2)+(y_pos[n]**2)+(z_pos[n]**2)))*delta_t)
                    y_angle = ((((z_pos[n]*x_velocity[n])-(x_pos[n]*z_velocity[n]))/((x_pos[n]**2)+(y_pos[n]**2)+(z_pos[n]**2)))*delta_t)
                    z_angle = ((((x_pos[n]*y_velocity[n])-(y_pos[n]*x_velocity[n]))/((x_pos[n]**2)+(y_pos[n]**2)+(z_pos[n]**2)))*delta_t)
                #Add the calculated values to the columns to create an array
                df = df.append(pd.Series([x_angle, y_angle, z_angle], index=df.columns), ignore_index = True)
            print(str(x_angle))
            #Add the old imported columns to the new data frame
            df['x_pos'] = list(TestData['x_pos'][1:])
            df['y_pos'] = list(TestData['y_pos'][1:])
            df['z_pos'] = list(TestData['z_pos'][1:])
            df['time'] = list(TestData['time'][1:])
            df['x_velocity'] = list(TestData['x_velocity'][1:])
            df['y_velocity'] = list(TestData['y_velocity'][1:])
            df['z_velocity'] = list(TestData['z_velocity'][1:])
            df['x_acceleration'] = list(TestData['x_acceleration'][1:])
            df['y_acceleration'] = list(TestData['y_acceleration'][1:])
            df['z_acceleration'] = list(TestData['z_acceleration'][1:])
            df['pressure'] = list(TestData['pressure'][1:])
            #Rearrange all the columns to the desired pattern
            df = df.reindex(['time','x_pos','y_pos','z_pos','pressure','x_velocity','y_velocity','z_velocity','x_acceleration','y_acceleration','z_acceleration','x_angle','y_angle','z_angle'], axis='columns')
            #Export the new data frame arrays into the old csv, replacing the old with the new
            df.to_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_data", "generated", csv_name), index = False)

    #Call the beginning function
    import_data(csv_name)


