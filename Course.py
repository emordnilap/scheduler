from Class import *



class Course():
    '''A class representing an entire course.'''
    def __init__(self, code, classes):
        '''(Course, str, list of Class) -> None
        
        Given the course code, and the list of Classes, transform them into
        Courses, defined by their code and separated into lectures,
        tutorials, and practicals.
        '''
        self._code = code
        self._lectures = {}
        self._tutorials = {}
        self._practicals = {}
        for clas in classes:
            ctype = clas.get_ctype()
            num = clas.get_num()
            if ctype is CType.LEC:
                lesson = self._lectures
            elif ctype is CType.TUT:
                lesson = self._tutorials
            else:
                lesson = self._practicals
            # If there is an existing class with the same number
            if num in lesson.keys():
                # Add the class onto the existing list of class
                lesson[num].append(clas)
            # If there is no existing class then create it
            # Or, if there is a different class
            else:
                # Map the class number to the list of Class
                lesson = {num: [clas]}
