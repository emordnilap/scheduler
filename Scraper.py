from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Class import *


def get_html(course):
    '''(list of str) -> list of BeautifulSoup

    Return the live UTSC timetable page's html code in BeautifulSoup
    format as well as which semester the course is in
    when given the desired, complete course code.

    REQ: 'course' must be a list of complete UTSC course codes,
         for example: MATA31 (not valid, as it is incomplete)
         for example: csca08h3s (valid; not case-sensitive)
    REQ: A downloaded Chrome driver at the specified path
    REQ: Internet access
    '''
    # todo remove chrome driver if possible
    # Creates a chrome driver (a browser)
    # Can be downloaded here:
    # https://sites.google.com/a/chromium.org/chromedriver/
    # Must be downloaded at 'path' directory
    path = r"C:\Chrome\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    url = "http://www.utsc.utoronto.ca/~registrar/scheduling/timetable"
    # Go to the url
    driver.get(url)
    # List that holds all soup objects
    soup_bowl = []
    # Go through all the course codes and store the soup objects
    for c in course:
        # Get the textbox to input course code, which has name='course2'
        input_box = driver.find_element_by_name('course2')
        # Clear the box of existing content
        input_box.clear()
        # Insert course code sans the last digit, as there are issues with it
        input_box.send_keys(c[:6])
        # Click the 'display by course' button to show all data,
        # which has name='submit2'
        display_by_course_button = driver.find_element_by_name('submit2')
        display_by_course_button.click()
        try:
            # Wait at most 5 seconds for the page to load a checkbox that
            # will only appear if the page loads completely
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'Enrl_ControlCheck')))
        except TimeoutException:
            print("Page took too long to load, consider increasing time.")
        # Get the html code of the complete page
        html = driver.page_source
        # Get the soup html code
        soup = BeautifulSoup(html, "html.parser")
        soup_bowl.append(soup)
    return soup_bowl


def get_info(soup, course):
    '''(BeautifulSoup, str) -> list of Class

    Return a Class object with all information only
    related to the provided course code when given a valid soup object
    and the valid course code.

    REQ: soup must be html code obtained from the UTSC timetable site
    REQ: course is a list of full course codes in string form
    '''
    # todo remove the course requirement above and allow for incorrect course codes, and return error message
    # Get all table rows in the page
    all_tr = soup.find_all('tr')
    # A switch that flips to True when the below loop starts
    # iterating over the corrent range of data
    on = False
    # A switch that flips to True when the specific course is found
    found = False
    # Initialization of the list to hold all the classes
    all_classes = []
    # Since lectures typically have multiple sessions, hold which
    # lecture number is currently being iterated over
    curr = None
    # Check one row at a time
    for tr in all_tr:
        # If a link tag is found, and the string of the link is
        # the course code without any whitespaces, that means the
        # course info has been found
        if tr.find('a') and \
                        tr.a.string.lower().replace(' ', '') == course.lower():
            found = True
        if on:
            # The first data holds the session (t)ype and (num)ber
            # For example, LEC01, TUT0026, PRA0002
            tnum = tr.contents[0].string
            # If there is no explicit session type and number, it means
            # it extends from the previous; otherwise save the current
            if tnum is None:
                tnum = curr
            else:
                curr = tnum
            # The second data holds the session date in the week
            # For example, MO, TH, FR
            date = tr.contents[1].string
            # The third data holds the starting time of the session
            # For example, 13:00, 16:30
            s_time = tr.contents[2].string
            # The fourth data holds the ending time of the session
            # For example, 19:00, 11:30
            e_time = tr.contents[3].string
            # The fifth data holds the location
            # For example, IC130, HW216, AA112
            room = tr.contents[4].string.replace(" ", "")
            # The sixth data holds the prof name, if applicable
            prof = tr.contents[5].string
            # The seventh data holds notes if they exist
            notes = tr.contents[6].string
            # Create a Class
            uclass = Class(tnum, date, s_time, e_time, room, prof, notes)
            # Add Class to the list that will hold all Classes
            all_classes.append(uclass)
        # If the loop doesn't reach the data, then check:
        # 1) The table row has a child, and if True,
        # 2) The table row's child has a string, and if True,
        # 3) The table row's child's string refers to the row
        # 4) The course has been found and this is not some other course
        #    right before the actual data
        if tr.contents is not None and tr.contents[0].string is not None \
                and 'Meeting Section' in tr.contents[0].string and found:
            # If conditions are true, that means the loop has reached
            # the current table row and now flip the switch
            on = True
    return all_classes

if __name__ == '__main__':
    # Enrolled courses
    courses = ['cscb36h3y', 'cscb09h3y']
    # Grab a list of all the html code corresponding to each course, in soup form
    soups = get_html(courses)
    all_info = []
    # Store each class in a list itself, then add it to the main list
    for i in range(len(soups)):
        all_info.append(get_info(soups[i], courses[i]))
    e = 0
    # First go through the courses
    for info in all_info:
        # Print the course code corresponding to the course
        print(courses[e])
        # Then go through each individual class
        for i in info:
            print(i)
        e += 1
