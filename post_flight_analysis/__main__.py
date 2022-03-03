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
import core.rotation
import core.stitches
import core.force_calc


def main():
    # Imports data. This will return a stuct containing the data in SI units and any metadata
    base_data, mdata = core.data_in.extract(mode="test")
    threshold = mdata["accel_range"]
    m_i = mdata["m_i"]
    m_f = mdata["m_f"]  
    C_D = mdata["C_D"] 
    A_f = mdata["A_f"]
    burn_time = mdata["burn_time"]
    # TODO: Add rest of metadata


    time = base_data[:, 0]

    accel_low = np.vstack((base_data[:, 1], base_data[:, 2], base_data[:, 3]))
    accel_high = np.vstack((base_data[:, 4], base_data[:, 5], base_data[:, 6]))
    accel = core.stitches.stitch(time, accel_low, accel_high, threshold)

    omega = np.vstack((base_data[:, 7], base_data[:, 8], base_data[:, 9]))
    compass = np.vstack((base_data[:, 10], base_data[:, 11], base_data[:, 12]))

    pressure = base_data[:, 13]

    pressure_alt = core.ISA_Altitude_gen.ISA_altitude(pressure)

    # TODO: Callibarte pressure
    # TODO: Callibrate angular position

    # Rotating vectors
    accel = core.rotation.rotate(omega,time,accel)

    vel_x = core.integrate.left_sum(time, accel_low[0])
    vel_y = core.integrate.left_sum(time, accel_low[1])
    vel_z = core.integrate.left_sum(time, accel_low[2])
    vel = np.asarray([vel_x, vel_y, vel_z])

    pos_x = core.integrate.left_sum(time, vel[0])
    pos_y = core.integrate.left_sum(time, vel[1])
    pos_z = core.integrate.left_sum(time, vel[2])
    pos = np.asarray([pos_x, pos_y, pos_z])


    force = core.force_calc.calculate_force(time, accel, m_i, m_f, burn_time)

    # TODO: Calculate aero forces

    # TODO: Calculate impulse

    # TODO: Calculate ISA and accel calculated altitude divergence

    return None


if __name__ == "__main__":
    main()
