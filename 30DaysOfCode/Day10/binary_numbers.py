# Day 10: Binary Numbers

# Given base-10 integer, n, converto to binary (base-2).
# Then find and print the maximum count(decimal) of consecutive 1's
# in the binary representation
# Ex: input = 5, output= 1 (base-10 5 = base-2 101) most consecutive ones is 1.

import sys


def convert_to_binary(decimal):
    binary_conversion = []
    while decimal > 0:
        remainder = decimal % 2
        binary_conversion.append(remainder)
        decimal = decimal / 2
    binary_conversion.reverse()
    return binary_conversion

def print_binary_number(binary_list):
    for digit in binary_list:
        print digit,
    print

def consecutive_ones(binary_list):
    current_count = 0
    max_count = 0
    for digit in binary_list:
        if digit == 1:
            # increase current count for ones
            current_count += 1
            # update max_count
            if current_count > max_count:
                max_count = current_count
        else:
            # reset count
            current_count = 0
    return max_count


# main
if __name__ == "__main__":
    # error check input

    n = int(raw_input().strip())

    #binary_conversion = convert_to_binary(n)
    binary_conversion = convert_to_binary(n)
    print_binary_number(binary_conversion)
    print consecutive_ones(binary_conversion)
