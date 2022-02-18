"""
TODO: Docstring
"""

# Formatted with Black, the uncompromising Python code formatter.

# Imports
import core.data_in
# import core.ang_vel
import core.ISA_altitude_gen
# import core.rotation
# import core.stitches


def main():
    # Imports data. This will return a stuct containing the data in SI units and any metadata
    base_data = core.data_in.extract(mode="test")
    time = base_data[:,0]
    # TODO: Extract flight data from struct
    # TODO: Extract metadata from struct

    # TODO: Separate acceleration data
    # TODO: Stitch low-G and high-G data together
    # TODO: Separate angular velocity data
    # TODO: Separate Compass data
    pressure = base_data[:,13]
    print(str(pressure))

    yee = core.ISA_Altitude_gen.ISA_altitude(pressure)


    print(str(yee[1]))

    # TODO: Callibarte pressure
    # TODO: Callibrate angular position

    # TODO: Rotate all vectors to GSI frame

    # TODO: Get velocity

    # TODO: Get position

    # TODO: Calculate Net force

    # TODO: Calculate aero forces

    # TODO: Calculate impulse

    # TODO: Calculate ISA and accel calculated altitude divergence

    return None


if __name__ == "__main__":
    main()
