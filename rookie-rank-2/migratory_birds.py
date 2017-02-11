# Migratory Birds

# A flock of b birds is flying accross the continent. Each bird has a type,
# and the different types are designated by the id numbers 1, 2, 3, 4, and 5.

# Given an array of n integers where each integer describes the type of bird
# find and print the type number of the most common bird.
# If two or more types of birds are equally common, choose the type with the
# smallest id number

import sys

n = int(raw_input().strip())
types = map(int, raw_input().strip().split())
print types

distribution = [0]*6
for kind in types:
    distribution[kind] +=1

max_type_count = 0
type_of_max = 0
for i, count in enumerate(distribution):
    if count > max_type_count:
        max_type_count = count
        type_of_max = i

# print distribution
# print "max count: ", max_type_count
# print "type: ", type_of_max
print type_of_max
