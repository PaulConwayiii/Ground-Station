"""
Test Data Generator Suite
Version: 1.0.0
Author(s): Paul Conway
Created for: Project Nova, a technical support team part of Cerberus, a subteam of the ERFSEDS club at ERAU Daytona Beach.

Description: This module creates test data for parabolic trajectories in accordance with Project Nova's needs.
"""

# Formatted with Black, the uncompromising Python code formatter.

import core.json_gen
import core.pos_gen
import os
import regex


def main():
    # TODO: Implement switch case to allow the user to select from a range of options, such as generate JSON, generate test data, etc.
    # Note: Switch cases are being implemented in Python 3.10, which is going to be released October 4th, 2021
    print(__doc__)
    file_state = False  # Does the file exist?
    while file_state == False:  # TODO: exception handling
        json_name = input(
            "Specify the name of a JSON file you would like to read from.\nIf no such file exists, you will be prompted if you would like to create it:\n"
        )
        # Regex matching so including file extension is optional
        # Finds all instances of the string between any character and .json
        if regex.findall(r'(.*)(?=.json)', json_name) == []:
            json_name = json_name + '.json'
        json_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "local_data", "json", json_name
        )
        if os.path.isfile(json_path) == False:
            pref_new = input(
                json_name + " does not exist, would you like to create it? (y/n)\n"
            )
            if pref_new.lower() == "y":
                core.json_gen.generate(json_name, json_path)
                file_state = True
            else:
                # TODO: Maybe add a way to escape out of this
                file_state == False
        else:
            file_state = True
    core.pos_gen.generate(json_path)

    return None


if __name__ == "__main__":
    main()
