# Day 4: Class vs. Instance
# Learn about the difference between a class and an instance.


# Write a Person class with an instance variable, age, and a constructor
# that takes an integer, initialAge, as a parameter.
# The age cannot be negative, if it is set to zero and print invalid message.
class Person:
    def __init__(self, initialAge):
        finalAge = initialAge
        if finalAge < 0:
            finalAge = 0
            print "Age is not valid, setting age to 0."
        self.age = finalAge

    # Performs the following
    # age < 13, print "You are young."
    # age >= 13, and age < 18, print "You are a teenager."
    # else, print "You are old."
    def amIOld(self):
        if self.age >= 18:
            print "You are old."
        elif self.age >= 13:
            print "You are a teenager."
        else:  # age 0 - 12
            print "You are young."

    # Increases the age by 1.
    def yearPasses(self):
        self.age += 1


# tests
testCount = int(raw_input())
for i in range(0, testCount):
    age = int(raw_input())
    person = Person(age)
    person.amIOld()
    for j in range(0, 3):
        person.yearPasses()
    person.amIOld()
    print("")
