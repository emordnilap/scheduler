from Class import *


class Course():
    '''A class representing an entire course.'''
    def __init__(self, code, classes):
        '''(Course, str, list of Class) -> None
        
        Given the course code, and the list of Classes, transform them into
        Courses, defined by their code and separated into lectures,
        tutorials, and practicals.
        '''
        self._code = code.upper()
        self._lectures = {}
        self._tutorials = {}
        self._practicals = {}
        self._sessions = [self._lectures, self._tutorials, self._practicals]
        for session in classes:
            ctype = session.get_ctype()
            num = session.get_num()
            # Check which type of class it is
            if ctype is CType.LEC:
                lesson = self._lectures
            elif ctype is CType.TUT:
                lesson = self._tutorials
            else:
                lesson = self._practicals
            # If there is an existing class with the same number
            if num in lesson.keys():
                # Add the class onto the existing list of class
                lesson[num].append(session)
            # If there is no existing class then create it
            # Or, if there is a different class
            else:
                # Map the class number to the list of Class
                lesson[num] = [session]
        # The length of each course per week (in hours)
        # Calculated by hours of lectures + tutorials + practicals
        self._length = 0
        for session in self._sessions:
            keys = list(session.keys())
            # If the dictionary of session is nonempty, get the length of a random session
            # If the session DNE, then its length is 0
            self._length += sum([x.get_length() for x in session[keys[0]]] if len(keys) != 0 else [])

    def get_length(self):
        return self._length

    def get_lec(self):
        return self._lectures

    def get_tut(self):
        return self._tutorials

    def get_pra(self):
        return self._practicals

    def get_code(self):
        return self._code

    def __repr__(self):
        lectures = ''
        tutorials = ''
        for l in self._lectures.values():
            lectures += str(l) + '\n\t\t'
        for t in self._tutorials.values():
            tutorials += str(t) + '\n\t\t'
        tu = (self._code, lectures, tutorials, self._practicals)
        return "Course code : {}\n\tLecture(s):\n\t\t{}\n\tTutorial(s):\n\t\t{}\n\tPractical(s):\n\t\t{}".format(*tu)