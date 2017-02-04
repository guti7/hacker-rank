# Arrays in two dimensions.

# Given a 6 x 6 2D array, A:
# Find the hourglass with the maximum sum of its values
# There are 16 hourglasses in A
# Hourglass: The subset of values with indices following the graphical pattern
#  a b c        1 1 1 0 0 0
#    d          0 1 0 0 0 0
#  e f g    A = 1 1 1 0 0 0
#               0 0 0 0 0 0
#               0 0 0 0 0 0
#               0 0 0 0 0 0

# Given a 6 x 6 matrix return the hourblass with the maximum sum
def max_sum_hourglass(matrix):
    all_sums = []
    for x in range(0, 4):
        for y in range(0, 4):
            current_sum = sum(matrix[x][y:y+3]) + matrix[x+1][y+1] \
             + sum(matrix[x+2][y:y+3])
            all_sums.append(current_sum)

    return max(all_sums)


# Given a 3 x 3 matrix returns the sum of its hourglass
def hourglass_sum(matrix_hourglass):
    sum = 0
    for index, row in enumerate(matrix_hourglass):
        for value in (row):
            sum += matrix_hourglass[1][1] if row == 1 else value
    return sum


# main
if __name__ == "__main__":
    import sys

    matrix_a = []
    # Get matrix A from user
    for array_i in xrange(6):
        # rows
        arr_temp = map(int, raw_input().strip().split(' '))
        # columns
        matrix_a.append(arr_temp)

    print max_sum_hourglass(matrix_a)
