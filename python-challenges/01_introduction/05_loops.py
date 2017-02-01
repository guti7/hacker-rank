# Read an integer N. For all non-negative integers i < N, print  i^2.

if __name__ == '__main__':
    n = int(raw_input())

    for i in range(0, n):
        print i**2
