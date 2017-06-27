from Course import Course
import itertools

def product(courses):
    '''(list of Course) -> list of tuple of tuple of list of Class
    
    Returns all the possible combinations of lectures, tutorials, and practicals
    from the given list of Courses.
    '''
    # the list that holds the entirety of possibilities
    all_schedules = []
    # the list that holds with a list of lectures, a list of tutorials, and a list of practicals
    schedule = []
    # a list that holds the cartesian product of the above
    schedules = []
    # a list that holds all Classes of a lecture, tutorial, or practical
    classes = []

    # Check each given course
    for course in courses:
        # Add all lectures to classes
        for e in course.get_lec().values():
            classes.append(e)
        # sometimes certain courses don't have tutorials or practicals
        if classes != []:
            # Added the list of all lectures of this course to schedule
            schedule.append(classes)
        # reset
        classes = []
        for e in course.get_tut().values():
            classes.append(e)
        if classes != []:
            schedule.append(classes)
        classes = []
        for e in course.get_pra().values():
            classes.append(e)
        if classes != []:
            schedule.append(classes)
        classes = []
        # cartesian product within the course itself
        schedules.append(list(itertools.product(*schedule)))
        # store that cartesian product
        all_schedules.append(schedules)
        # reset
        schedule = []
        schedules = []

    # flatten list
    all_schedules = [s[0] for s in all_schedules]

    # cartesian product of all courses
    all_schedules = list(itertools.product(*all_schedules))

    return all_schedules
