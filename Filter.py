# The class that filters out classes based off of the user's requirements

import Class
import Time


def filters(courses, filter):
    '''(list of Course, dict of str:Time)
    
    When given a list of Course and a dictionary mapping the string date
    (MO, TU, etc.) to the Time ('13:00-14:00', etc.), return a list of Course
    that contains none of the properties of the provided filter. If a certain
    filter is impossible, then ignore it and return an error message as well.

    REQ: the string in filter can contain only MO, TU, WE, TH, FR
    '''
