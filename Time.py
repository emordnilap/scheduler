class Time():
    '''A class representing a duration of time, and NOT a single point in time'''

    def __init__(self, start, end):
        '''(Time, str, str) -> None

        Given two strings representing starting and ending times, convert them
        to Time format, which is defined to be four integers.

        That is, given, say, '12:06' and '13:52', it will be converted to
        12, 6, 13, 52, representing the starting time in minutes and hours,
        and the other representing the ending time similarly.

        REQ: Time does not pass through midnight, i.e. 23:00 - 00:40 will not be allowed
        REQ: start comes before end
        '''
        # Store the raw string
        self.rstart = start
        self.rend = end
        # Index of the starting time's colon
        s_colon = start.index(':')
        # Index of the ending time's colon
        e_colon = end.index(':')
        # Take the integer value of everything after the colon for starting time
        self.start_minute = int(start[s_colon + 1:len(start)])
        # Take the integer value of everything before the colon for starting time
        self.start_hour = int(start[:s_colon])
        # Same as above, just for the ending time
        self.end_minute = int(end[e_colon + 1:len(end)])
        self.end_hour = int(end[:e_colon])

    def get_length(self):
        return get_duration(self.start_hour, self.start_minute, self.end_hour, self.end_minute)

    def __str__(self):
        return self.rstart + ' - ' + self.rend

    def get_start(self):
        return self.rstart

    def get_end(self):
        return self.rend

    def is_conflicting(self, time):
        '''(Time, Time) -> bool

        When given a Time, determine whether they are disjoint. If so,
        then return False. If not, then return True.

        '''
        # Compare hours to see which Time starts first
        if self.start_hour < time.start_hour:
            first = self
        elif self.start_hour > time.start_hour:
            first = time
        # If their starting hours are the same, compare the minutes
        else:
            if self.start_minute < time.start_minute:
                first = self
            elif self.start_minute > time.start_minute:
                first = time
            # If the minutes are the same, then they definitely overlap, thus conflict
            else:
                return True
        # Set the other time to a new variable
        if first == self:
            second = time
        else:
            second = self

        # Get the difference between the starting time of both times
        diff_hour, diff_minute = get_duration(first.start_hour, first.start_minute, second.start_hour, second.start_minute)
        # Get the duration of the first starting time
        dur_hour, dur_minute = first.get_length()

        # Initialization
        is_conflicting = None

        # If the difference between both starting times is larger than
        # the duration of the first starting time, then there is no conflict
        if dur_hour < diff_hour:
            is_conflicting = False
        # If the converse is true, then there is a conflict
        elif dur_hour > diff_hour:
            is_conflicting = True
        # If the length in hours is the same, then the conflict depends
        # on the minutes
        else:
            # Similar to above
            if dur_minute < diff_minute:
                is_conflicting = False
            elif dur_minute > diff_minute:
                is_conflicting = True
            # If the duration in difference and duration in time are the same,
            # then there is no conflict
            else:
                is_conflicting = False

        return is_conflicting


def get_duration(start_hour, start_minute, end_hour, end_minute):
    '''(int, int, int, int)

    Return the duration, in hours and minutes, when provided starting
    times and ending times

    REQ: in general, start time must come before end time
    REQ: the start time cannot be before midnight while the end time is after

    '''
    # If there are more minutes in the endtime then simply subtract
    # the minutes from the starttime to get the result
    if end_minute >= start_minute:
        length_minute = end_minute - start_minute
        length_hour = end_hour - start_hour
    # If not, then subtract one from end_hour then add 60 to
    # end_minute, since it will 'borrow' minutes from the hour
    else:
        length_minute = end_minute + 60 - start_minute
        length_hour = end_hour - 1 - start_hour
    return length_hour, length_minute
