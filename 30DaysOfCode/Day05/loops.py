# Day 5: Loops
# Use loops to do some math

# Given an integer n, print its ten first multiples
# print: "n x i = result", each on a new line.


#!/bin/python

import sys

Nmultiples = 10

n = int(raw_input().strip())

for i in range(1, Nmultiples + 1):
    print"%s x %s = %s" %(n, i, n * i)
