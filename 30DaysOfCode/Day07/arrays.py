# Day 7: Arrays
# Learn about the array data structure.

# Given an array A, of N integers, print A's elements in reverse
# order as a single line separated by one space.

import sys

n = int(raw_input().strip())

array = map(int, raw_input().strip().split(' '))
# print ("reverse? %r") % array.reverse()
for element in reversed(array):
    print element,
