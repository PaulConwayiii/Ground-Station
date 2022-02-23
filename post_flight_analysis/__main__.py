"""
TODO: Docstring
"""

# Formatted with Black, the uncompromising Python code formatter.

# Imports
import numpy as np
import core.data_in
import core.integrate
# import core.ang_vel
import core.ISA_Altitude_gen
# import core.rotation
import core.stitches


def main():
    # Imports data. This will return a stuct containing the data in SI units and any metadata
    base_data = core.data_in.extract(mode="test")
    threshold = 8  # TODO: remove when metadata extraction is implemented

    time = base_data[:, 0]

    accel_low = np.vstack((base_data[:, 1], base_data[:, 2], base_data[:, 3]))
    accel_high = np.vstack((base_data[:, 4], base_data[:, 5], base_data[:, 6]))
    accel = core.stitches.stitch(time, accel_low, accel_high, threshold)

    omega = np.vstack((base_data[:, 7], base_data[:, 8], base_data[:, 9]))
    compass = np.vstack((base_data[:, 10], base_data[:, 11], base_data[:, 12]))

    pressure = base_data[:, 13]

    # pressure_alt = core.ISA_Altitude_gen.ISA_altitude(pressure)

    # TODO: Callibarte pressure
    # TODO: Callibrate angular position

    # TODO: Rotate all vectors to GSI frame

    vel = core.integrate.left_sum(time, accel_low[0])
    print(str(vel))

    # TODO: Get position

    # TODO: Calculate Net force

    # TODO: Calculate aero forces

    # TODO: Calculate impulse

    # TODO: Calculate ISA and accel calculated altitude divergence

    return None


if __name__ == "__main__":
    main()
