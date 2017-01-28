# Make School OOP Coding Challenge Python Problem 5
import sys


# Implement Animal superclass
class Animal(object):
    # Initializer
    def __init__(self, name, food):
        self.name = name
        self.favoriteFood = food

    # Sleep
    def sleep(self):
        print "%s sleeps for 8 hours" % self.name

    # Eat
    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if self.favoriteFood == food:
            print "YUM! %s wants more %s" % (self.name, food)


# Implement Tiger class as a subclass of Animal
class Tiger(Animal):
    def __init__(self, name):
        super(Tiger, self).__init__(name, "meat")

# Implement Bear class as a subclass of Animal
class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name, "fish")

    def sleep(self):
        print "%s hibernates for 4 months" % self.name


# Tests
def test():
    def getline():
        # Read a line from stdin and strip whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the animals
    for count in range(animalCount):
        # Get the animal's species, name and food.
        species = getline()
        name = getline()
        food = getline()
        animal = None
        # Check what animal's species
        if species == "tiger":
            # Create Tiger object
            animal = Tiger(name)
        elif species == "bear":
            # Create a Bear object
            animal = Bear(name)
        else:
            # Create an Animal object
            animal = Animal(name, "kibble")
        # Test the animal's instance methods
        animal.eat(food)
        animal.sleep()

# main
if __name__ == "__main__":
    test()
