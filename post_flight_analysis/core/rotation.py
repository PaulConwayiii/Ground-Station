# TODO: Clean imports
import numpy as np
# import exceptions


def rotate(omega, step, R_frame, nose_axis="z"):
    """
    Expresses R_frame in terms of an inertial frame based on an angular velocity vector.
     parameters:
       omega:
           Type: 3 element nested list. Each list contains omega around an axis
           Units: rad/sec
           Expresses angular velocity vector of R_frame relative to an inertial frame
           TODO: Make thus use an numpy array
       step:
           Type: list
           Units: sec
           duration of rotation expressed by omega
       R_frame:
           Type: 3 element nested list. Each list contains vectors along a certain axis
           TODO: Make this use an numpy array
       nose_axis (optional):
           Type: string
           Values: 'x', 'y', 'z'
           Expressed which axis is pointing towards the nose (NOT IMPLEMENTED).
           The remaining two axis will be oriented such that the frame is right-handed

     Outputs:
       3 element list
       contains the unit vectors of R_frame after rotation in terms of the inertial frame
       TODO: Make this use an numpy array

    Raises:
        TODO: fill this out
    """

    # TODO: error checking inputs
    # TODO: omega is a 3 element vector?
    # TODO: R_frame is a 9 element array with columns having a magnitude of 1?

    # TODO: implement nose axis selection. The program is written such that the nose points towards z
    # For other axes, change the vectors so that z points towards the nose, perform the calculations,
    # then change back to the original orientation.
    match nose_axis:
        case "x":
            raise NotImplementedError(
                "Nose axis selection has not been implemented. Only supports z oriented nose"
            )
        case "y":
            raise NotImplementedError(
                "Nose axis selection has not been implemented. Only supports z oriented nose"
            )
        case "z":
            pass

    RR_x = np.zeros((len(step),))
    RR_y = np.zeros((len(step),))
    RR_z = np.zeros((len(step),))

    # These are not really Euler angles (unless it's a special case where they happen to be)
    for n,s in enumerate(step):
        alpha = omega[0][n] * s
        beta = omega[1][n] * s
        gamma = omega[2][n] * s


        # It's faster to do this once rather than compute these trig functions 12 times
        c_alpha = np.cos(alpha)
        s_alpha = np.sin(alpha)
        c_beta = np.cos(beta)
        s_beta = np.sin(beta)
        c_gamma = np.cos(gamma)
        s_gamma = np.sin(gamma)

        # Rotation matricies
        # Don't ask how I got these its fucking magic or something, or linear algebra...
        Q_1 = np.array([[1, 0, 0], [0, c_alpha, -s_alpha], [0, s_alpha, c_alpha]])
        Q_2 = np.array([[c_beta, 0, s_beta], [0, 1, 0], [-s_beta, 0, c_beta]])
        Q_3 = np.array([[c_gamma, -s_gamma, 0], [s_gamma, c_gamma, 0], [0, 0, 1]])
        # This matrix combines all rotations
        Q = np.matmul(np.matmul(Q_1, Q_2), Q_3)

        """
        # Rotated vectors
        i_rotated = np.matmul(Q, R_frame[0])
        j_rotated = np.matmul(Q, R_frame[1])
        k_rotated = np.matmul(Q, R_frame[2])
        """

        # Rotated vector
        raw_vec = [R_frame[0][n],R_frame[1][n],R_frame[2][n]]
        rot_vec = np.matmul(Q,raw_vec)

        RR_x[n] = rot_vec[0]
        RR_y[n] = rot_vec[1]
        RR_z[n] = rot_vec[2]

    return [RR_x,RR_y,RR_z]
