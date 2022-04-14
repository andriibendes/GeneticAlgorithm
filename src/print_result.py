from tabulate import tabulate

from data import *


def print_frame(frame, time_id):
    time = time_slots[time_id]
    w = time['week']
    d = time['day']
    t = time['time']
    print(f"Week {w}, {d}, {t}\n")
    data = []

    for room_id in range(len(frame)):
        if frame[room_id][1] == -1:
            data.append([room_id + 1, None, None, None])
        else:
            groups_st = ", ".join([groups[g]['name'] for g in frame[room_id][0]])
            te = teachers[frame[room_id][1]]['name']
            c = courses[frame[room_id][2]]['name']
            ct = courses[frame[room_id][2]]['type']
            data.append([room_id + 1, groups_st, te, c + ' (' + ct + ')'])

    print(tabulate(data, headers=["Classroom", "Group", "Teacher", "Course"]))


def print_schedule(schedule):
    for i in range(len(schedule)):
        print_frame(schedule[i], i)
        print("\n")
