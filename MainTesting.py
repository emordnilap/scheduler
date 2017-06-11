import Course

# Enrolled courses
courses = ['cscb36h3y', 'cscb09h3y']
# initialization of Course
course = []
# Grab a list of all the html code corresponding to each course, in soup form
soups = Course.get_html(courses)
all_info = []
# Store each class in a list itself, then add it to the main list
for i in range(len(soups)):
    all_info.append(Course.get_info(soups[i], courses[i]))
e = 0
# First go through the courses
for info in all_info:
    # Print the course code corresponding to the course
    print(courses[e])
    # Then go through each individual class
    for i in info:
        print(i)
    # Add new course to list of Course
    course.append(Course(courses[e], info))
    e += 1
