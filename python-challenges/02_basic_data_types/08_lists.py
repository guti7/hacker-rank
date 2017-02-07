# Initialize your list and read in the value of n followed by n lines of
# commands where each command will be of the 7 types listed below.
# Iterate through each command in order and perform the corresponding
# operation on your list.
# commands: insert, print, remove, append, sort, pop, and reverse

if __name__ == '__main__':
    N = int(raw_input())
    list = []

    while N > 0:
        N -= 1
        #print "%r" % N
        data = raw_input().split()
        if data[0] == "print":
            print list
        elif data[0] == "insert":
            #print "insert(%f, %d)" % (float(data[1]), float(data[2]))
            list.insert(int(data[1]), int(data[2]))
        elif data[0] == "remove":
            list.remove(int(data[1]))
        elif data[0] == "append":
            list.append(int(data[1]))
        elif data[0] == "sort":
            list.sort()
        elif data[0] == "pop":
            list.pop()
        elif data[0] == "reverse":
            list.reverse()
