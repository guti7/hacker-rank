# Read two integers and print two lines.
# The first line should contain integer division,  a // b.
# The second line should contain float division, a / b.

from __future__ import division
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print a // b
print a / b
