t = int(raw_input())
for _ in range(t):
    line = raw_input()
    first = ""
    second = ""

    for index, char in enumerate(line):
        if (index & 1) == 0:
            first += char
        else:
            second += char
    print first, second
