from Time import *

class Class:
    def __init__(self, ctype, day, start, end, room, prof, notes):
        self.ctype = ctype
        self.day = 'N/A' if day is None else day
        self.time = Time(start, end)
        self.room = 'N/A' if room is None else room
        self.prof = 'N/A' if prof is None else prof
        self.notes = 'N/A' if notes is None else notes

    def __str__(self):
        return 'Session: ' + self.ctype + " | Day: " + self.day + \
               " | Start: " + self.time.get_start() + " | End: " + self.time.get_end() + \
               " | Room: " + self.room + " | Prof: " + self.prof + \
               " | Notes: " + self.notes
