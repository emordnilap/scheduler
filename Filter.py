from Class import Class, Day


def schedule_filter(all_schedules, filter):
    '''(list of tuple of tuple of list of Class, dict of Day:Time) -> list of tuple of tuple of list of Class
    
    When given a set of set of Class and a dictionary mapping the date
    (MO, TU, etc.) to the Time ('13:00-14:00'), return a set of set of Class
    that contains none of the properties of the provided filter. If a certain
    filter is impossible, then ignore it and return an error message.
    
    If Day is mapped to None, it means that any class that is on any time of 
    Day should not be included.
    '''
    accepted_schedules = []
    # Look through all possible schedules
    for schedule in all_schedules:
        # Whether there is a conflict with the given filters
        # If true, then exclude the schedule
        conflict = False
        # Look through all the courses in a given schedule
        for course in schedule:
            # Look through the sessions in the course (session = LEC, TUT, etc.)
            for session in course:
                # Look through each class in the session
                for classes in session:
                    # Look through the filters
                    for day in filter:
                        # If it's a full-day filter
                        if filter[day] is None:
                            # If any of the classes contain this day then
                            # there will exist a conflict
                            if session.get_day() == day:
                                conflict = True
                        else:
                            # If the days and the times match, then there's a conflict
                            if session.get_day() == day and session.get_time().is_conflicting(
                                    filter[day]):
                                conflict = True
        # Only add the schedule if there are no conflicts
        if not conflict:
            accepted_schedules.append(schedule)

    return accepted_schedules


def _minimize_days(all_schedules, days=1):
    '''
    (set of set of Class) -> set of set of Class
    (set of set of Class, int) -> set of set of Class
    
    REQ: 1 <= days < 5
    
    Returns a set of set of Class representing all schedules with at least
    one day without any classes.
    
    Optional parameter days: the minimum number of days without classes,
    which, as stated above, is by default and minimally one.
    '''
    # INCOMPLETE
    accepted_schedules = set()
    all_days = {{Day.MO: None}, {Day.TU: None}, {Day.WE: None}, {Day.TH: None},
                {Day.FR: None}}
    for day in all_days:
        accepted_schedules.add(filter(all_schedules, day))

    return accepted_schedules
