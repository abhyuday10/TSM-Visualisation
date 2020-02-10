import numpy as np
import random
from random import randint
import copy
import matplotlib.pyplot as plt
import seaborn as sb
from map import *
import time

no_of_generations = 250
lower_limit = 0.2
N = 10
pop_size = 200
how_many_to_kill = 50
prob_mut = 0.00001


def initialise_map(lower_limit):
    # N is the number of pubs
    # random.random() generates a random float X ~ Unif([0,1)), we define lower_limit to avoid zeros

    our_map = np.zeros((N, N))

    # the adjacency matrix is a real symmetric matrix with zero entries along the diagonal

    for i in range(0, N):
        for j in range(0, i):  # do not include i since the diagonal is zero
            our_map[i][j] = random.random() * 10000
            our_map[j][i] = our_map[i][j]

    return our_map


def create_new_route():
    start = np.array([0])

    intermediate_steps = np.random.permutation(np.arange(1, N - 1))

    end = np.array([N - 1])

    temp = np.append(start, intermediate_steps)
    route = np.append(temp, end)

    return route


def crossover(a, b):
    crossover_point = randint(1, N - 1)

    index_a = 0
    index_b = 0

    for i in range(0, N):
        if (a == crossover_point)[i] == True:
            index_a = i
        if (b == crossover_point)[i] == True:
            index_b = i

    a_head = a[:index_a]
    a_tail = b[index_a:]

    new_a = np.append(a_head, a_tail)

    b_head = b[:index_b]
    b_tail = a[index_b:]

    new_b = np.append(b_head, b_tail)

    child = []
    if (len(new_a) >= N):
        child = new_a

    return child


def mutate(a, prob):
    if random.random() > prob:
        i = random.randint(1, len(a) - 2)
        j = random.randint(1, len(a) - 2)

        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    return a


def fitness(a, our_map):
    score = 0

    for i in range(0, N - 1):
        score += our_map[a[i]][a[i + 1]]

    return score


def create_generation(pop_size, our_map):
    population = []

    for i in range(0, pop_size):
        population.append(create_new_route())

    return population


def score_population(population, our_map):
    scores = []

    for i in range(0, len(population)):
        scores += [fitness(population[i], our_map)]

    return scores


def best_in_population(population, our_map):
    best = sort_population(population, our_map)[0]
    best_route = population[best]

    return best_route


def fitness_of_best_in_population(population, our_map):
    fit = fitness(best_in_population(population, our_map), our_map)

    return fit


def sort_population(population, our_map):
    scores = score_population(population, our_map)

    np_scores = np.array(scores)

    return np_scores.argsort()


def thanos(how_many_to_kill, population, our_map):
    ranked_pop = sort_population(population, our_map)
    survival_of_the_fittest = ranked_pop[: (len(population) - how_many_to_kill)]

    return survival_of_the_fittest


def fuck(population, our_map):
    fittest = thanos(how_many_to_kill, population, our_map)
    children = []

    for i in range(0, len(fittest), 2):
        child_1 = crossover(population[i], population[i + 1])
        child_1 = mutate(child_1, prob_mut)
        children.append(child_1)

    while (len(children) < pop_size):
        new_route = create_new_route()
        children.append(new_route)

    return children


def main():
    # our_map = initialise_map(lower_limit)
    names_of_locations_temp = ["kelseys", "the fat pug", "the town house", "the old library", "the clarendon",
                               "the benjamin satchwell", "murphy's bar", "The Royal Pug", "the white house",
                               "The Drawing Board"]
    names_of_locations = [name.lower() for name in sorted(names_of_locations_temp)]
    generator = MapGenerator(names_of_locations)
    locations = generator.decodeLocations()

    num_to_object = {}
    object_to_num = {}
    for counter, location_object in enumerate(locations):
        num_to_object[counter] = location_object
        object_to_num[location_object] = counter

    our_map = generator.adjacency_matrix_generator()
    #

    population = create_generation(pop_size, our_map)

    route_over_time = []
    fitnesses = []

    for i in range(0, no_of_generations):
        route_over_time.append(best_in_population(population, our_map))
        fitnesses.append(fitness_of_best_in_population(population, our_map))
        fuck(population, our_map)

        population = fuck(population, our_map)

    for i, current_route in enumerate(route_over_time):
        print(i, current_route)
    for current_route in route_over_time[-10:]:
        locations_to_render = [num_to_object[x] for x in current_route]
        generator.renderLocations(locations_to_render)
        time.sleep(3)


    plt.plot(np.arange(0, no_of_generations), fitnesses)
    plt.ylabel('fitness')
    plt.xlabel('no. of generations')


main()
#Test commit
#Test commit 2
