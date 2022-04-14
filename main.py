from data import *
from src.genetic import genetic_algorithm
from src.print_result import print_schedule

print("Courses: ", courses)
print("Teachers: ", teachers)
print("Groups: ", groups)
print("Classrooms:", classrooms)

schedule = genetic_algorithm(time_slots, classrooms, courses, groups, teachers)
print_schedule(schedule)
