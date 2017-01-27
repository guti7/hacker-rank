# Make School OOP Coding Challenge Python Problem 2
import sys

# A Tiger's favorite food is meat
favoriteFood = "meat"

# Write a function named sleep that takes a name variable as an argument.
# This function should print "<name> sleeps for 8 hours" each time it's called.
def sleep(name):
    print name, "sleeps for 8 hours"

# Write a function named eat that takes two arguments: name and food.
# This function should print: "<name> eats <food>"
# If the animal eats their favorite food then also print:
# "YUM! <name> wants more <food>"
def eat(name, food):
    print "%s eats %s" % (name, food)
    if food == favoriteFood:
        print "YUM! %s wants more %s" % (name, food)

# This code tests the eat and sleep functions
def test():
    def getline():
        # Read a line from standard input and strip surrounding whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's name and food to eat
        name = getline()
        food = getline()
        # Test the eat and sleep functions
        eat(name, food)
        sleep(name)

if __name__ == "__main__":
    test()
