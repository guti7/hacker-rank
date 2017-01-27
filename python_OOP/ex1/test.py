# This code tests the sleep function
def test():
    def getline():
        # Read a line from standard input and strip surrounding whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's name
        name = getline()
        # Test the sleep function
        sleep(name)


if __name__ == "__main__":
    test()
