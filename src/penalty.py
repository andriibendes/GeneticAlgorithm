import numpy as np

from data import *


def count_total_hours(schedule, groups):
    total_hours = {}

    for g in groups:
        total_hours[g['id']] = {c: 0 for c in g['courses']}

    for frame in schedule:
        for room in frame:
            if room[1] != -1:
                groups_id = room[0]
                course_id = room[2]
                for g_id in groups_id:
                    total_hours[g_id][course_id] += 1

    return total_hours


def penalty_hours(schedule, groups, courses):
    """
    Sum of abs differences between the hours needed for the course and actual.
    """
    penalty_hours_score = 0
    total_hours = count_total_hours(schedule, groups)
    for group in total_hours.values():
        for course_id in group:
            needed_hours = courses[course_id]['hours']
            actual_hours = group[course_id]
            if needed_hours > actual_hours:
                penalty_hours_score += needed_hours - actual_hours
    return penalty_hours_score


def groups_in_frame(frame):
    res = []
    for room in frame:
        if room[1] != -1:
            res.extend(room[0])
    return res


def penalty_gaps(schedule, lessons_per_day):
    """
    Sum of gaps in each group's schedule.
    """
    score = 0

    if lessons_per_day <= 2:
        return score

    day = np.zeros(lessons_per_day, dtype=object)

    schedule_iterator = iter(schedule)
    frame = 0

    while not (frame is None):
        for i in range(lessons_per_day):
            frame = next(schedule_iterator, None)
            if frame is None:
                break
            day[i] = frame
        if not (frame is None):
            groups_st = groups_in_frame(day[0])
            groups_fin = groups_in_frame(day[-1])
            groups_mid = groups_in_frame(day[1])
            for g in groups_st:
                if g in groups_fin and g not in groups_mid:
                    score += 1
    return score


def fitness_function(schedule, lessons_per_day=3):
    """
    Rate the fitness of this individual.
    """
    score = 0
    score += penalty_hours(schedule, groups, courses) * 5
    score += penalty_gaps(schedule, lessons_per_day)
    return score
