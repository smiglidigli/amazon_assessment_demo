#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    steps = 0
    for ix in range(len(arr)):
        while arr[ix] != ix + 1:
            if arr[ix] != ix + 1:
                tmp = arr[arr[ix] - 1]
                arr[arr[ix] - 1] = arr[ix]
                arr[ix] = tmp
                steps += 1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
