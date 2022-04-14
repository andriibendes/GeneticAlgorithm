import random

import numpy as np

from src.frame_generator import generate_frame
from src.penalty import fitness_function
from src.pool_functions import random_elements
from src.schedule_generator import generate_population


def simple_crossover(a, b, pos=-1):
    """
    One-point crossover.
    """
    if pos == -1:
        pos = random.randint(0, a.size)
    new_a = np.hstack((a[:pos], b[pos:]))
    new_b = np.hstack((b[:pos], a[pos:]))
    return new_a, new_b


def crossover(a, b, points=1):
    """
    Multi-point crossover between two members of population.
    """
    new_a = np.copy(a)
    new_b = np.copy(b)
    for i in range(points):
        new_a, new_b = simple_crossover(new_a, new_b)
    return new_a, new_b


def mutation(a, prob=0.01):
    """
    Performs a mutation on a with certain probability.
    """
    new_a = a.copy()
    for frame_id in range(new_a.size):
        if random.choices((True, False), [prob, 1 - prob])[0]:
            new_a[frame_id] = generate_frame()
    return new_a


def next_gen(prev, parents_count=10, survive_count=1, crossover_points=None, mut_prob=0.01):
    """
    Generates the next population.
    """
    if crossover_points is None:
        crossover_points = [1, 5]

    population = len(prev)
    parents_gen = prev[:parents_count]
    new_gen = prev[:survive_count].copy()

    while len(new_gen) < population:
        parents = random_elements(parents_gen, 2)
        children = crossover(*parents, random.randint(*crossover_points))

        new_gen.append(mutation(children[0], mut_prob))
        new_gen.append(mutation(children[1], mut_prob))

    # Sorting in regards to penalty score.
    new_gen = sorted(new_gen[:population], key=lambda schedule: fitness_function(schedule))
    best = [str(fitness_function(s)) for s in new_gen[:5]]

    print("Best 5 of this generation: ", ", ".join(best))
    return new_gen


def genetic_algorithm(time_slots, rooms, courses, groups, teachers):
    """
    Performs a genetic algorithm to find an optimal schedule.
    """
    population = generate_population(20, time_slots, rooms, courses, groups, teachers)
    print("The first generation was created")

    gen_count = 0
    while fitness_function(population[0]) != 0:
        gen_count += 1
        print("Generation #", gen_count)
        population = next_gen(population)

    return population[0]
