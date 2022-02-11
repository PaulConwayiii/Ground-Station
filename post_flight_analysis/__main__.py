"""
TODO: Docstring
"""

# Formatted with Black, the uncompromising Python code formatter.

# Imports
import core.data_in


def main():
    # Imports data. This will return a stuct containing the data in SI units and any metadata
    base_data = data_in.extract()
    # Extract flight data from struct
    # Extract metadata from struct

    # Separate acceleration data
    # Separate angular velocity data
    # Separate Compass data
    # Separate Pressure data

    # Callibarte pressure
    # Callibrate angular position

    # Rotate all vectors to GSI frame

    # Get velocity

    # Get position

    # Calculate Net forces

    # Calculate aero forces

    # Calculate impulse

    # Calculate ISA and accel calculated altitude divergence


    return None


if __name__ == "__main__":
    main()
