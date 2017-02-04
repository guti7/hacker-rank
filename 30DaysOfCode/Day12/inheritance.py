# Day 12: Inheritance
# Delving into Inheritance

# Given two classes with templates, Person and Student,
# complete the Student class.
# Grading sale: T >= 0, D >= 40, P >= 55, A >= 70, E >= 80, and O >= 90 <= 100

# constructor with first name, last name, id, and array of test scores.

# Write a method that calculates a Student's test score average and
# return the grade as a character from the grading scale.


class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = int(idNumber)

    def printPerson(self):
        print 'Name:%s, %s' % (self.lastName, self.firstName)
        print 'ID:%d' % self.idNumber


class Student(Person):

    # constructor with first name, last name, id, and array of test scores.
    def __init__(self, firstName, lastName, idNumber, testScores):
        # super(Student, self).__init__(firstName, lastName, idNumber)
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = testScores

    # Calculates a Student's test score average and
    # returns the grade as a character from the grading scale.
    def calculate(self, testScores):
        # print '%r' % testScores
        # sum = 0
        # for score in testScores:
        #     sum += score
        # return sum / len(testScores)
        total = sum(testScores)
        average = total / len(testScores)

        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 70:
            return 'A'
        elif average >= 55:
            return 'P'
        elif average >= 40:
            return 'D'
        else:
            return 'T'

# main
if __name__ == '__main__':
    line = raw_input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(raw_input())
    scores = map(int, raw_input().split())
    student = Student(firstName, lastName, idNum, scores)
    student.printPerson()
    letter_grade = student.calculate(scores)
    print "Grade:", letter_grade
