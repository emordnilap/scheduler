import Scraper
from Course import Course, Day
from Filter import *
from Time import *

# Enrolled courses
from Product import product

courses = ['cscb07h3y', 'cscb36h3y', 'matb24h3y', 'stab52h3y']
# initialization of Course
course = []
# Grab a list of all the html code corresponding to each course, in soup form
soups = Scraper.get_html(courses)
all_info = []
# Store each class in a list itself, then add it to the main list
for i in range(len(soups)):
    all_info.append(Scraper.get_info(soups[i], courses[i]))
e = 0
# First go through the courses
for info in all_info:
    # Print the course code corresponding to the course
    # print(courses[e])
    # Then go through each individual class
    for i in info:
        pass
        # print(i)
    # Add new course to list of Course
    course.append(Course(courses[e], info))
    e += 1

all_schedules = product(course)
print("Total combinations: " + str(len(all_schedules)))

all_schedules = schedule_filter(all_schedules, {Day.TU: None, Day.MO: Time("13:00", "14:00"), Day.TH: Time("09:00", "14:00")})

print("Total combinations: " + str(len(all_schedules)))

for schedule in all_schedules:
    print(schedule)