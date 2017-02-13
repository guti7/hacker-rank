import sys

wordHR = 'hackerrank'

def isSubsequence(wordHR, test_string):

    length_HR = len(wordHR)
    length_test = len(test_string)

    # Base Cases
    if length_HR == 0:    return True
    if length_test == 0:    return False

    # # If last characters of two strings are matching
    # if wordHR[length_HR - 1] == test_string[length_test - 1]:
    #     # modify string
    #     return isSubsequence(wordHR[:-1], test_string[:-1])
    #
    # # If last characters are not matching
    # return isSubsequence(wordHR, test_string[:-1])
    # If last characters of two strings are matching
    if wordHR[0] == test_string[0]:
        # modify string
        return isSubsequence(wordHR[1:], test_string[1:])

    # If last characters are not matching
    return isSubsequence(wordHR, test_string[1:])


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    if isSubsequence(wordHR, s):
        print "YES"
    else:
        print "NO"
