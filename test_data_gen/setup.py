"""
Installing nonstandard module dependancies
Version: 1.0.0
Author(s): Paul Conway

Description: Installs modules not in the standard library.
Pulls the list of non standrd libraries from non_std_modules.txt
"""

import subprocess
import sys
import importlib
import os


def install(module):
    # Creates a subprocess to install module
    # Essentially running the command "python3 -m pip install <module_name>"
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])
    return None


def check_module(package):
    # Checks to see if the specified module is installed
    if importlib.util.find_spec(package) == None:
        return False
    else:
        return True


def setup():
    # Opens file with module names
    with open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'non_std_modules.txt'
        ),
        'r',
    ) as req_list:
        # Reading file line by line
        req_lines = req_list.readlines()
        for module_name in req_lines:
            # Checks each module to see if it's installed
            if module_name != '\n':
                if check_module(module_name.rstrip('\n')) == False:
                    install(module_name)
    return None


if __name__ == '__main__':
    setup()
