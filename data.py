import random

from src.pool_functions import random_elements


def generate_courses():
    names = ["Calculus", "Programming", "Software Development", "Foreign Language", "Systems Programming",
             "Life Science", "Systems Design", "Linear Algebra"]
    types = ["Lecture", "Seminar"]
    hours_range = [10, 20]

    courses = []
    id = 0

    for name in names:
        for t in types:
            course = {
                "id": id,
                "name": name,
                "type": t,
                "hours": random.randint(*hours_range)
            }
            courses.append(course)
            id += 1
    return courses


# noinspection PyShadowingNames
def generate_teachers(courses):
    names = ["Hal Abelson", "Adam Belay", "Fadel Adib", "Mohammad Alizadeh", "Jacob Andreas", "Marc A. Baldo"]
    density = [1, 3]
    teachers = []

    for id in range(len(names)):
        teachers.append({
            "id": id,
            "name": names[id],
            "courses": []
        })

    teachers_len = len(teachers)

    for course_id in range(len(courses)):
        dens = random.randint(*density)
        teach = random_elements(range(teachers_len), dens)
        for t in teach:
            teachers[t]['courses'].append(course_id)

    return teachers


def generate_groups(courses):
    group_count = 6
    students_range = [25, 35]
    course_quantity = [5, 7]
    groups = []
    courses_count = len(courses)
    for i in range(group_count):
        groups.append({
            "id": i,
            "name": "Group " + str(i + 1),
            "students": random.randint(*students_range),
            "courses": random_elements(range(courses_count), random.randint(*course_quantity))
        })
    return groups


def generate_rooms(init=[]):
    rooms = []
    if init:
        for id in range(len(init)):
            rooms.append({
                "id": id,
                "size": init[id]
            })
    else:
        n = 6
        size_range = [30, 90]
        for i in range(n):
            rooms.append({
                "id": i,
                "size": random.randint(*size_range)
            })
    return rooms


def generate_time_slots():
    time_slots = []
    id = 0
    for week in range(12):
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            for time in ["8:40 - 10:15", "10:35 - 12:10", "12:20 - 13:55"]:
                time_slots.append({
                    'id': id,
                    'week': week + 1,
                    'day': day,
                    'time': time
                })
                id += 1

    return time_slots


courses = generate_courses()
teachers = generate_teachers(courses)
groups = generate_groups(courses)
# classrooms = generate_rooms([30, 30, 30, 60, 90, 40])
classrooms = generate_rooms()
time_slots = generate_time_slots()