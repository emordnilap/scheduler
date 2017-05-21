from Time import *
from enum import Enum


class Class:
    '''A class representing a single class, such as a lecture, tutorial, or practical.'''
    def __init__(self, ctype, day, start, end, room, prof, notes):
        # Take the first three characters of the class type, and compare it
        # to the value of existing enum. If they match, then set them equal.
        self._ctype = [c for c in CType if c.value == ctype[:3]][0]
        # Class number identification
        self._cnum = ctype[3:]
        # Class number in integer form
        self._num = int(self._cnum)
        self._day = 'N/A' if day is None else day
        self._time = Time(start, end)
        self._room = 'N/A' if room is None else room
        self._prof = 'N/A' if prof is None else prof
        self._notes = 'N/A' if notes is None else notes
        self._time_length = self._time.get_time_length()
        self._length = self._time.get_length()

    def __str__(self):
        return 'Session: ' + self._ctype.value + self._cnum + " | Day: " + self._day + \
               " | Start: " + self._time.get_start() + " | End: " + self._time.get_end() + \
               " | Room: " + self._room + " | Prof: " + self._prof + \
               " | Notes: " + self._notes

    def __repr__(self):
        return self.__str__()

    def get_cnum(self):
        return self._cnum

    def get_num(self):
        return self._num

    def get_length(self):
        return self._length

    def get_time_length(self):
        return self._time_length

    def get_ctype(self):
        return self._ctype

    def get_day(self):
        return self._day

    def get_time(self):
        return self._time


class CType(Enum):
    LEC = 'LEC'
    TUT = 'TUT'
    PRA = 'PRA'
