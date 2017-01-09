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
             optimisation_cycles, eval_f):

    # vector initialisation
    vec = np.full(vec_len, 0.5, dtype=float)

    # initialise population
    population = np.empty((pop_size, vec_len), dtype=float)
    scores = [None for _ in range(pop_size)]

    for i in range(optimisation_cycles):
        # solution vectors generation
        for j in range(pop_size):
            for k in range(vec_len):
                population[j][k] = get_num(vec[k])
            # vector evoluation
            scores[j] = eval_f(population[j])
        # best vectors selection
        sorted_res = sorted(zip(scores, population), key=lambda x:x[0], reverse=True)
        best = sorted_res[:num_best_vec_to_update_from]
        worst = sorted_res[-num_worst_vec_to_update_from:]
        print best, vec

        # update vector
        for v in best:
            vec += 2 * learn_rate * (v[1] - 0.5)
        for v in worst:
            vec -= 2 * neg_learn_rate * (v[1] - 0.5)

        # vector correction if elements outside [0, 1] range
        for i in range(vec_len):
            if vec[i] < 0:
                vec[i] = 0
            elif vec[i] > 1:
                vec[i] = 1
    return best[0][1] #TODO powinien zwracać najlepszy z wszystkich, nie z tej tury


if __name__ == '__main__':
    def eval_fun(nums, bits):
        assert len(nums) == len(bits)
        return sum(nums[i]*bits[i] for i in range(len(nums)))
    data = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13]
    print optimize(0.02, 0.02, 10, 2, 2, 13, 25, functools.partial(eval_fun, data))

