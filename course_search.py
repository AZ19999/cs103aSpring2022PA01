'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from re import T
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
open (filter by courses that are open)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        
        #code that we wrote
        
        elif command in ['c', 'course']:
            subject=input("enter a course")
            schedule =  schedule.course([course])
            return
        elif command in ['i', 'instructor']:
            subject=input("enter an instructor")
            schedule =  schedule.instructor([subject])
            return
        elif command in ['t', 'title']:
            subject=input("enter a course title")
            schedule = schedule.title([subject])
            return
        elif command in ['d', 'description']:
            phrase = input("enter a phrase:")
            schedule = schedule.description(phrase)
        elif command in ['i', 'independent_study']:
            status = input["T (independent study) or F (not independent study"]
            if status == 'T':
                status = 'true'
            else:
                status = 'false'
            schedule = schedule.independent(status)
        elif command in ['o', 'open']:
            status = input("Do you want to see courses that are a. Open, b. Open with consent required, c. Closed [a/b/c]:")
            while status not in ['a','b','c']:
                  status = input("Please enter a valid option: a. Open, b. Open with consent required, c. Closed [a/b/c]:")  
            if status == 'a':
                status = 'Open'
            elif status == 'b':
                status = 'Open Consent Req.'
            elif status == 'c':
                status = 'Closed'
            schedule = schedule.open(status)
            
        #end of our section

        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])


if __name__ == '__main__':
    topmenu()

