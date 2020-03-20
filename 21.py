#!/bin/python

import math
import os
import random
import re
import sys
import copy
import operator

# Complete the minimumBribes function below.
def minimumBribes(q):
    q_copy = copy.deepcopy(q)
    bribes = {}
    sorted_array = [x for x in range(1, len(q) + 1)]

    print(map(operator.sub, sorted_array, [x for x in q]))

    while map(operator.sub, sorted_array, [x for x in q]) != [0 for x in q]:
        for ix in range(len(q) - 1):
            if q[ix] > q[ix + 1]:
                q_copy[ix] = q[ix + 1]
                q_copy[ix + 1] = q[ix]
                k = max(q[ix], q[ix + 1])
                if k in bribes:
                    bribes[k] += 1
                else:
                    bribes[k] = 1
                q = q_copy

    print(sum([v for k,v in bribes.items()]))
    for k,v in bribes.items():
        if v >= 3:
            print("Too chaotic")
            return

if __name__ == '__main__':
    t = int("2
5
2 1 5 3 4
5
2 5 1 3 4")

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
