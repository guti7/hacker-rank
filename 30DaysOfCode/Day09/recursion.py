# Exercise 9: Recursion
# Learning and practicing Recursion.
# factorial(N) = { 1                     N<=1
#                { N x factorial(N - 1)  otherwise

# Write a factorial function that takes a positive integer, N as a parameter and
# print the result of N!

# recursive function that calculates N!
def factorial(N):
    if N <= 1: return N
    else: return N * factorial(N - 1)


if __name__ == "__main__":
    # take integer from user
    n = int(raw_input("Provide an integer: ").strip())
    print factorial(n)
