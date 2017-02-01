# Basic Data Types: List Comprehensions (Hacker Rank)

# You are given three integers X, Y and Z representing the maximum dimensions
# of a cuboid along with an integer N.
# Print all possible coordinates given by (i, j, k) on a 3D grid
# where the sum of i + j + k is not equal to N.
import sys

def calculate_cuboid_coordinates(x, y, z, n):
    # how to break up list comprehensions?
    return [[a, b, c] for a in range(x + 1) for b in range(y + 1)
            for c in range(z + 1) if a + b + c != n]
            # use \ to break up long lines to multiple lines
            # or just return if within brackets

if __name__ == '__main__':
    # x = int(raw_input().strip())  # maybe use loop?
    # y = int(raw_input().strip())
    # z = int(raw_input().strip())
    # n = int(raw_input().strip())
    input_count = 4
    x, y, z, n = (int(raw_input().strip()) for _ in range(input_count))

    print calculate_cuboid_coordinates(x, y, z, n)
