# Day 14: Scope
# Find the maximum absolute difference in a set of given integers and
# print it to console


# Complete the Difference class
class Difference(object):
    # Constructor takes an array of integers
    def __init__(self, array):
        self.elements = array  # self.__elements = array ?

    # finds the maximum absolute difference betweeen 2 numbers in N elements
    def compute_difference(self):
        self.maximumDifference = 0

        e = self.elements
        for i in range(len(e) - 1):
            for j in range(i + 1, len(e)):
                difference = abs(e[i] - e[j])
                if difference > self.maximumDifference:
                    self.maximumDifference = difference


# main
if __name__ == '__main__':
    # get number of elements
    # n = raw_input()
    # read elements
    elements = [int(e) for e in raw_input().strip().split(' ')]

    # print maximum absolute difference
    difference = Difference(elements)
    difference.compute_difference()
    print 'final: ', difference.maximumDifference
