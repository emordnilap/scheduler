from Time import *
from enum import Enum


class Class:
    '''A class representing a single class, such as a lecture, tutorial, or practical.'''
    def __init__(self, ctype, day, start, end, room, prof, notes):
        # Take the first three characters of the class type, and compare it
        # to the value of existing enum. If they match, then set them equal.
        self.ctype = [c.name for c in CType if c.value == ctype[:3]][0]
        self.day = 'N/A' if day is None else day
        self.time = Time(start, end)
        self.room = 'N/A' if room is None else room
        self.prof = 'N/A' if prof is None else prof
        self.notes = 'N/A' if notes is None else notes

    def __str__(self):
        return 'Session: ' + str(self.ctype) + " | Day: " + self.day + \
               " | Start: " + self.time.get_start() + " | End: " + self.time.get_end() + \
               " | Room: " + self.room + " | Prof: " + self.prof + \
               " | Notes: " + self.notes


class CType(Enum):
    LEC = 'LEC'
    TUT = 'TUT'
    PRA = 'PRA'
