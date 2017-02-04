# Find the Second Largest Number

# You are given N numbers. Store them in a list and
# find the second largest number

# main
if __name__ == '__main__':
    # check for valid integer given
    n = int(raw_input().strip())
    array = map(int, raw_input().split())

    array.sort()
    array.reverse()
    
    max_value = array[0]
    for value in array:
        if value < max_value:
            print value
            break
