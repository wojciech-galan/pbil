#! /usr/bin/python
# -*- coding: utf-8 -*-

import functools
import numpy as np

from pbil.optimizer import optimize

if __name__ == '__main__':
    def eval_fun(nums, bits):
        assert len(nums) == len(bits)
        return sum(nums[i]*bits[i] for i in range(len(nums)))
    data = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, 15, 16, -17, -18, -19]
    l = []
    print optimize(0.02, 0.02, 10, 2, 2, len(data), 25, functools.partial(eval_fun, data), vec_storage=l)
    # if you're interested in the evolution of the population vector, uncomment the lines below
    # print '--------------------------------------------------------------------------'
    # print np.asarray(l, float)