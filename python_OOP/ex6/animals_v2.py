# Make School OOP Coding Challenge Python Problem 6

import sys


# Animal class
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


# Tiger class
class Tiger(Animal):
    def __init__(self, name):
        super(Tiger, self).__init__(name, "meat")


# Bear class
class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name, "fish")

    def sleep(self):
        print "%s hibernates for 4 months" % self.name


# Unicorn class
class Unicorn(Animal):  # implement Initializer and override sleep
    def __init__(self, name):
        super(Unicorn, self).__init__(name, "marshmallows")

    def sleep(self):
        print "%s sleeps in a cloud" % self.name


# Giraffe class
class Giraffe(Animal):  # implement Initializer and override eat
    def __init__(self, name):
        super(Giraffe, self).__init__(name, "leaves")

    # call the superclass's eat to reuse code.
    def eat(self, food):
        super(Giraffe, self).eat(food)
        if self.favoriteFood != food:
            print "YUCK! %s spits out %s" % (self.name, food)


# Bee class
class Bee(Animal):  # initializer and override eat and sleep
    def __init__(self, name):
        super(Bee, self).__init__(name, "pollen")

    def eat(self, food):
        super(Bee, self).eat(food)
        if self.favoriteFood != food:
            print "YUCK! %s spits out %s" % (self.name, food)

    def sleep(self):
        print "%s never sleeps" % self.name


# Tests
def test():
    def getline():
        # Read line from stdin and strip whitespace
        return sys.stdin.readline().strip()
    # Get number of animals
    animalCount = int(getline())
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's info
        species = getline()
        name = getline()
        food = getline()
        animal = None
        # Check the species and create respective object
        if species == "tiger":
            animal = Tiger(name)
        elif species == "bear":
            animal = Bear(name)
        elif species == "unicorn":
            animal = Unicorn(name)
        elif species == "giraffe":
            animal = Giraffe(name)
        elif species == "bee":
            animal = Bee(name)
        else:
            # Create a generic Animal
            animal = Animal(name, "kibble")
        # Test animals instance methods
        animal.eat(food)
        animal.sleep()

# main
if __name__ == "__main__":
    test()
