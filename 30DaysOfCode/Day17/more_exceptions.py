"""Calculator class."""
# Day 17: More Exceptions:
# Practice throwing and propagation an exception.

# Task:
# Write a Calculator class with a single method: power(int, int).


class Calculator():

    # Returns the n^p, if n or p are negative throws exception.
    def power(self, n, p):
        """
        Take two integers, n and p, and returns the integer of n^p
        if either n or p is negative, then the method throws an exception.
        """

        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return n ** p


# main
if __name__ == '__main__':
    myCalculator = Calculator()
    T = int(raw_input())
    for i in range(T):
        n, p = map(int, raw_input().split())
        try:
            ans = myCalculator.power(n, p)
            print(ans)
        except Exception, e:
            print e
