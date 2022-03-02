import numpy as np

def calculate_mass(t, m_i, m_f, t_S, t_B):
    mass = (((m_f-m_i)/(t_B-t_S))*(t-t_B))+m_i
    return mass

def calculate_force(t, a, m_i, m_f, B, t_S=1):
    t_B = t_S + B
    force_arr = np.array([np.zeros([len(t),1]),
                             np.zeros([len(t),1]),
                             np.zeros([len(t),1])])
    temp_arr = np.zeros([len(t),1])

    for index in range(len(a[0])):
        x_accel_arr = a[0]
        x_accel = x_accel_arr[index]
        mass = calculate_mass(t[index], m_i, m_f, t_S, t_B)
        temp_arr[index] = mass * x_accel
    force_arr[0] = temp_arr

    for index in range(len(a[1])):
        y_accel_arr = a[1]
        y_accel = y_accel_arr[index]
        mass = calculate_mass(t[index], m_i, m_f, t_S, t_B)
        temp_arr[index] = mass * y_accel
    force_arr[1] = temp_arr

    for index in range(len(a[2])):
        z_accel_arr = a[2]
        z_accel = z_accel_arr[index]
        mass = calculate_mass(t[index], m_i, m_f, t_S, t_B)
        temp_arr[index] = mass * z_accel
    force_arr[2] = temp_arr
    
    return force_arr