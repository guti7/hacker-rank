#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here


# finds the minimum absolute difference betweeen 2 numbers in N elements
def compute_difference(array):

    minimumDifference = sys.maxint

    e = array
    e.sort()
    for i in range(len(e) - 1):
        difference = abs(e[i] - e[i + 1])
        if difference < minimumDifference:
            minimumDifference = difference
    return minimumDifference


min_diff = compute_difference(a)

print min_diff
