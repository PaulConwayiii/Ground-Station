"""
Position Generator
Version: 1.0.0
Author(s): Paul Conway

Description: This file generates a series of points based off the parameters contained in a JSON file.
The points follow a parabolic trajectory assuming standard gravity and zero air resistance
"""

# Formatted with Black, the uncompromising Python code formatter.

import json
import os
import math
import pandas as pd


def generate(json_path):
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
        a = json_data["x_weight"]
        b = json_data["y_weight"]
        c = 9.80665  # Standard gravitational acceleration
        h = json_data["altitude"]
        noise_level = json_data["noise_level"]
        json_name = json_data["json_name"]
        steps_per_second = json_data["steps_per_second"]
        message_num = 0
    df = pd.DataFrame(columns=["message_num", "time", "x_pos", "y_pos", "z_pos"])
    # df.to_csv(os.path.join(os.path.dirname(json_path), os.path.pardir,'generated', json_name +'.csv'), index=False)
    root = math.sqrt(h / c)
    for time_stamp in range(
        -1, math.ceil(2 * steps_per_second * root + math.sqrt(steps_per_second)), 1
    ):
        time_val = (time_stamp / steps_per_second) - root
        x_pos = a * (time_val + root)
        y_pos = b * (time_val + root)
        z_pos = h - (c * (time_val ** 2))
        message_num = message_num + 1
        if z_pos > 0:  # Needed in case z becomes negative
            x_last = x_pos
            y_last = y_pos
            z_last = z_pos
        elif (
            message_num > 1
        ):  # If z < 0, sets the position such that it does not change (rocket has hit the ground)
            x_pos = x_last
            y_pos = y_last
            z_pos = 0
        elif (
            message_num <= 1
        ):  # If z < 0 for values of t close to the start, should be ignored and position should be 0
            x_pos = x_last = 0
            y_pos = y_last = 0
            z_pos = z_last = 0
        if math.remainder(message_num, 100) == True:
            print(str(message_num))
        df = df.append(
            pd.Series(
                [
                    message_num,
                    (time_val + root + (1 / steps_per_second)),
                    x_pos,
                    y_pos,
                    z_pos,
                ],
                index=df.columns,
            ),
            ignore_index=True,
        )
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print('Position data generation complete!')
    df.to_csv(
        os.path.join(
            os.path.dirname(json_path), os.path.pardir, "generated", json_name + ".csv"
        ),
        index=False,
    )
    print(
        'Position data saved to file: ' + os.path.dirname(json_path),
        os.path.pardir,
        "generated",
        json_name + ".csv",
    )
