# Make School OOP Coding Challenge Python Problem 3

import sys

# Create a class called Tiger.
# It should contain two instance variables: name and favoriteFood
# It should contain eat and sleep instance methods
# Write an initializer that takes a name.
class Tiger(object):
    # initializer
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

    # Sleep prints "<name> sleeps for 8 hours".
    def sleep(self):
        print "%s sleeps for 8 hours" % self.name

    # Eat takes an argument for food.
    # It prints: "<name> eats <food>"
    # If the animal eats their favorite food then also prints:
    # "YUM! <name> wants more <food>"
    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if self.favoriteFood == food:
            print "YUM! %s wants more %s" % (self.name, food)


# Test the Tiger class and its instance methods
def test():
    def getline():
        # Read a line from stdin and strip whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the input
    for count in range(animalCount):
        # Get the animal's name and food
        name = getline()
        food = getline()
        # Create a Tiger object and test its instance methods
        tiger = Tiger(name)
        tiger.eat(food)
        tiger.sleep()

if __name__ == "__main__":
    test()
