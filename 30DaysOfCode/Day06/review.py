# Day 6: Let's Review
# Expanding knowledge of string and combining it with loops

# Given a string S, of length N that is indexed from 0 to N-1,
# print its even-indexed and odd-indexed characters as
# 2 space-separated strings on a single line.
# Example: "Hacker" -> "Hce  akr"

import sys

wordCount = int(raw_input().strip())
for i in range(wordCount):
    word = raw_input()
    even = ""
    odd = ""
    for j in range(len(word)):
        if j % 2 == 0:
            even += word[j]
        else:
            odd += word[j]
    print "%s  %s" % (even, odd)
