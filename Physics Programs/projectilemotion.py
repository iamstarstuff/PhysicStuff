import numpy as np

# Acceleration due to gravity in m/s
g = 9.8  

def x_component(u,theta,time):
    """
    Arguments:
        u : initial velocity in m/s
        theta : angle from horizontal in degrees 
    Returns:
        Horizontal component of motion
    """
    max_time = (2*u*np.sin(np.deg2rad(theta)))/g #max time
    if time <= max_time:
        return u*np.cos(np.deg2rad(theta))*time
    else:
        print("The time is more than time of flight of projectile")

def y_component(u,theta,time):
    """
    Arguments:
        u : initial velocity in m/s
        theta : angle from horizontal in degrees
    Returns:
        Vertical component of motion
    """
    max_time = (2*u*np.sin(np.deg2rad(theta)))/g #max time
    if time <= max_time:
        return u*np.sin(np.deg2rad(theta))*time - 0.5*g*time**2
    else:
        print("The time is more than time of flight of projectile")

def time_of_flight(u,theta):
    """
    Arguments:
        u : initial velocity in m/s
        theta : angle from horizontal in degrees
    Returns :
        Time of flight of projectile
    """
    return (2*u*np.sin(np.deg2rad(theta)))/g

def range(u,theta):
    """
    Arguments :
        u : initial velocty in m/s
        theta : angle from horizontal in degrees
    Returns:
        Range of projectile
    """
    return (u**2*np.sin(2*np.deg2rad(theta)))/g

def max_height(u,theta):
    """
    Arguments :
        u : initial velocity in m/s
        theta : angle from horizontal in degrees
    Returns :
        Maximum height of projectile
    """
    return (u**2*(np.sin(np.deg2rad(theta)))**2)/(2*g)

def area_under_path(u,theta):
    """
    Arguments :
        u : initial velocty in m/s
        theta : angle from horizontal in degrees
    Returns:
        Area under the path of projectile
    """
    t = np.deg2rad(theta)
    return (2*u**4*(np.sin(t))**3*np.cos(t))/(3*g**2)


    