"""
TODO: Docstring
"""

# Formatted with Black, the uncompromising Python code formatter.

# Imports
import graphlib
import matplotlib.pyplot as plt

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
    accel_mag = [np.sqrt(accel[0][i]**2 + accel[1][i]**2 + accel[2][i]**2) for i,_ in enumerate(time)]

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
    vel_mag = [np.sqrt(vel[0][i]**2 + vel[1][i]**2 + vel[2][i]**2) for i,_ in enumerate(time)]

    pos_x = core.integrate.left_sum(time, vel[0])
    pos_y = core.integrate.left_sum(time, vel[1])
    pos_z = core.integrate.left_sum(time, vel[2])
    pos = np.asarray([pos_x, pos_y, pos_z])
    xy_pos = [np.sqrt(pos[0][i]**2 + pos[1][i]**2) for i,_ in enumerate(time)]
    pos_mag = [np.sqrt(pos[0][i]**2 + pos[1][i]**2 + pos[2][i]**2) for i,_ in enumerate(time)]

    force = core.force_calc.calculate_force(time, accel, m_i, m_f, burn_time)
    force_mag = [np.sqrt(force[0][i]**2 + force[1][i]**2 + force[2][i]**2) for i,_ in enumerate(time)]

    # TODO: Calculate aero forces

    # TODO: Calculate impulse

    # TODO: Calculate ISA and accel calculated altitude divergence

    # Plottting happens here:

    #Acceleration (x, y, x, mag w.r.t. t)
    plt.subplot(3,3,1)
    plt.plot(time,accel[0])
    plt.plot(time,accel[1])
    plt.plot(time,accel[2])
    plt.plot(time,accel_mag)
    plt.legend(["x","y","z","net"])
    plt.title("Acceleration, m/s^2")

    #Down Range (x, y, mag w.r.t. t)
    plt.subplot(3,3,2)
    plt.plot(time,pos_x)
    plt.plot(time,pos_y)
    plt.plot(time,xy_pos)
    plt.legend(["x","y","net"])
    plt.title("Down Range, m")

    #Velocity (x, y, z, mag w.r.t. t)
    plt.subplot(3,3,4)
    plt.plot(time,vel_x)
    plt.plot(time,vel_y)
    plt.plot(time,vel_z)
    plt.plot(time,vel_mag)
    plt.legend(["x","y","z","net"])
    plt.title("Velocity, m/s")

    #Altitude (from Pressure and acceleration w.r.t. t)
    plt.subplot(3,3,5)
    plt.plot(time,pos_z)
    plt.plot(time,pressure_alt)
    plt.legend(["accel_alt, pressure_alt"])
    plt.title("Altitude, m")

    #Position (x, y, z w.r.t. t)
    plt.subplot(3,3,7)
    plt.plot(time,pos_x)
    plt.plot(time,pos_y)
    plt.plot(time,pos_z)
    plt.plot(time,xy_pos)
    plt.legend(["x","y","z","net"])
    plt.title("Position, m")

    #Force (x, y, z w.r.t. t)
    plt.subplot(3,3,8)
    plt.plot(time,force[0])
    plt.plot(time,force[1])
    plt.plot(time,force[2])
    plt.plot(time,force_mag)
    plt.legend(["x","y","z","net"])
    plt.title("Force, m")

    #Plot Formatting
    plt.tight_layout(pad = 0.005)
    plt.show()
    return None


if __name__ == "__main__":
    main()
