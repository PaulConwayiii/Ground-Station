"""
JSON Generator
Version: 1.0.0
Author(s): Paul Conway

Description: This file generates a JSON file containing the given user inputs.
"""

# Formatted with Black, the uncompromising Python code formatter.

import json


def generate(json_name, json_path):
    # TODO: input checking
    x_weight = float(input("Specify an X axis weight: "))
    y_weight = float(input("Specify an Y axis weight: "))
    altitude = float(input("Specify a max altitude: "))
    noise_level = float(input("Specify a noise level: "))
    steps_per_second = int(input("Specify how many steps per second: "))
    notes = input("Notes: ")
    json_data = {
        "json_name": json_name[0:-5],
        "x_weight": x_weight,
        "y_weight": y_weight,
        "altitude": altitude,
        "noise_level": noise_level,
        "steps_per_second": steps_per_second,
        "notes": notes,
    }
    with open(json_path, "w") as outfile:
        json.dump(json_data, outfile)
