# Day 8: Dictionaries and Maps

# Learn about key-value pair mappings using Map or a Dicitionary structure

# Given n names and phone numbers, assemble a phone book that maps
# friend's names to their respective phone numbers

# Query for names and print "name=phoneNumber" for each line, if not found
# print "Not found"
# Note: Continues to read lines until EOF.
import sys

n = int(raw_input().strip())

phone_book = {}

for i in range(0, n):  # range max in not inclusive
    info_array = list(raw_input().strip().split())
    # Build dictionary structure
    phone_book[info_array[0]] = info_array[1]
    print info_array
    print phone_book

# for line in sys.stdin:
#     name = line.strip()
#     if name in phone_book:
#         print '%s=%s' % (name, phone_book[name])
#     else:
#         print "Not found"

while True:
    try:
        name = raw_input()
        if name in phone_book:
            print "%s=%s" % (name, phone_book[name])
        else:
            print 'Not Found'
    except:
        break
