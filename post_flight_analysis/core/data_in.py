"""
TODO: Docstring
"""

# Imports
import numpy as np


def extract(mode="live"):
    match mode:
        case "live":
            # Get unprocessed data
            # TODO: grab raw data based on input parameters

            # Get parameters/metadata
            # TODO: Separate metadata from flight data.
            #   ISA correction
            #   Motor parameters
            #   Rocket parameters
            #   Sensor parameters

            # Convert raw sensor voltages to SI values if neccesary
            # TODO: Implement ability to translate from voltage to SI eqiv
            # TODO: Implement ability to change between modes.

            # Apply low pass filters
            # TODO: Implement low pass filters based in metadata and component specs

            pass
        case "test":
            # TODO: Implement
            # This is only for testing purposes. Will export pre-made data

            # This is just placeholder data. Better data should be made
            rows = 3000
            data = np.zeros((rows, 11))
            t = np.linspace(0, 3, rows)
            for n in t:
                data[n, 0] = n
                data[n, 1:11] = np.random((1, 10))
        case _:
            # TODO: Raise exception
            pass

    # Return struct containing flight data and metadata
    return data
