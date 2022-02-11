"""
TODO: Docstring
"""

# Imports


def extract():
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

    # Apply stitching to any data
    # TODO: Call relevant stitching functions

    # TODO: This is probably not neccesary and is only adding complications
    def stitch(func_type):
        """
        TODO: Docstring
        """
        # Any stitching functions go here
        match func_type:
            case "accel":
                # TODO: implement stitching algorithm
                pass
            case _:
                # TODO: Raise error
                pass

        def accel():
            # For stitching acceleration data
            # There is a low G and high G sensor.
            # If the values reported by the low G sensor exceed spec, replace with high G values.
            pass

        pass

    # Return struct containing flight data and metadata
    return None
