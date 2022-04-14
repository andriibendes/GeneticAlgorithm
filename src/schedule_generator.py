import numpy as np

from src.frame_generator import generate_frame


def generate_schedule(time_slots, rooms, courses, groups, teachers):
    schedule = np.zeros_like(time_slots, dtype=object)
    for i in range(len(time_slots)):
        schedule[i] = generate_frame(rooms, courses, groups, teachers)
    return schedule


def generate_population(quantity, time_slots, rooms, courses, groups, teachers):
    pool = [generate_schedule(time_slots, rooms, courses, groups, teachers) for _ in range(quantity)]
    return pool
