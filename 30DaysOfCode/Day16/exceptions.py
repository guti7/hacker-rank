# Day 16: Exception - String to Integer

# Getting started with Exceptions by learning how to parse an integer from
# a string and printing error message.

# Task: Read a strig, S, and print its integer value
# If S cannot be converted print 'Bad String'.


if __name__ == '__main__':
    s = raw_input().strip()

    try:
        integer = int(s)
    except ValueError:
        print 'Bad String'
