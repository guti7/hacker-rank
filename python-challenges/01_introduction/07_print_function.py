# Read an integer N. Without using any string methods,
# try to print the following:
# 123...N
# Note that "..." represents the values in between.

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())

    for i in range(1, n + 1):
        print(i, end='')
