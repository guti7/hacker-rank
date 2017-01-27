# Make School OOP Coding Challenge Python Problem 4
import sys


# Create a class Bear
# instance variables: name and favoriteFood
# initializer: contains one argument name and favoriteFood to "fish"
# eat: is the same to Tiger
# sleep: print "<name> hibernates for 4 months"
class Bear(object):
    # Initializer
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"

    # Sleep
    def sleep(self):
        print "%s hibernates for 4 months" % self.name

    # Eat
    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if self.favoriteFood == food:
            print "YUM! %s wants more %s" % (self.name, food)


# Tiger Class
class Tiger(object):
    # Initializer
    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

    # Sleep
    def sleep(self):
        print "%s sleeps for 8 hours" % self.name

    # Eat
    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if self.favoriteFood == food:
            print "YUM! %s wants more %s" % (self.name, food)


# Test Tiger and Bear classes and respective instance methods
def test():
    def getline():
        # Read line from stdin and strip whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the input
    for count in range(animalCount):
        # Get the animal's species, name and food to eat
        species = getline()
        name = getline()
        food = getline()
        # Check what species the animal is
        if species == "tiger":
            # Create a Tiger object and test its instance methods
            tiger = Tiger(name)
            tiger.eat(food)
            tiger.sleep()
        elif species == "bear":
            # Create a Bear object and test its instance methods
            bear = Bear(name)
            bear.eat(food)
            bear.sleep()
        else:
            print("Unknown animal species:{}".format(species))


# main
if __name__ == "__main__":
    test()
