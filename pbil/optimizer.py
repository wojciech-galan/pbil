#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import functools

import numpy as np


def get_num(proba):
    """
    Returns 0 or 1 depending on proba value
    :param proba: num between (but including) [0, 1] - probability of 1
    """
    if random.random() < proba:
        return 1
    return 0


def optimize(learn_rate, neg_learn_rate, pop_size, num_best_vec_to_update_from, num_worst_vec_to_update_from, vec_len,
             optimisation_cycles, eval_f, eps=0.01, vec_storage=None):
    """

    :param learn_rate: rate of pushing the population vector (vec) towards each of the best individuals
    :param neg_learn_rate: similar to learn rate, but pushes the vector away from the worst individuals
    :param pop_size: num of individuals in population
    :param num_best_vec_to_update_from: how many best individuals will be used to update population vector
    :param num_worst_vec_to_update_from: how many worst individuals will be used to update population vector
    :param vec_len: length of the population vector
    :param optimisation_cycles: num of optimisation cycles
    :param eval_f: function for individual's fitness evaluation
    :param eps: population vector will be pushed away eps from extreme values (0, 1)
    :param vec_storage: storage for population vectors from each turns, should implement "append" method
    :return: best binary vector. If many vectors have the same fitnesses, returns the one, that appeared most early
    """

    # vector initialisation
    vec = np.full(vec_len, 0.5, dtype=float)

    # initialise population
    population = np.empty((pop_size, vec_len), dtype=int)
    scores = [None for _ in range(pop_size)]

    # initialise best result
    best_of_all = [-float("inf"), None]

    # store vec?
    if vec_storage is not None:
        vec_storage.append(list(vec))

    for i in range(optimisation_cycles):
        # solution vectors generation
        for j in range(pop_size):
            for k in range(vec_len):
                population[j][k] = get_num(vec[k])
            # vector evaluation
            scores[j] = eval_f(population[j])
        # best vectors selection
        sorted_res = sorted(zip(scores, population), key=lambda x:x[0], reverse=True)
        best = sorted_res[:num_best_vec_to_update_from]
        worst = sorted_res[-num_worst_vec_to_update_from:]

        # update best_of_all
        if best_of_all[0] < best[0][0]:
            best_of_all = (best[0][0], list(best[0][1]))

        # update vector
        for v in best:
            vec += 2 * learn_rate * (v[1] - 0.5)
        for v in worst:
            vec -= 2 * neg_learn_rate * (v[1] - 0.5)

        # vector correction if elements outside [0, 1] range
        for i in range(vec_len):
            if vec[i] < 0:
                vec[i] = 0 + eps
            elif vec[i] > 1:
                vec[i] = 1 - eps

        # store vec?
        if vec_storage is not None:
            vec_storage.append(list(vec))

    return best_of_all[1]


