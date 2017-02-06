# Day 13: Abstract Classes
# Extending inheritance to Abstract Classes

# Given a Book class and a Solution class, write a MyBook class that
# does the following:

# Inherits from Book
# Has a parameterized constructor taking 3 parameters: title, author, and price
# Implements the Book class' abstract display() and prints
# the book's instance variables in its own line.

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass

# MyBook
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print 'Title: %s' % self.title
        print 'Author: %s' % self.author
        print 'Price: %s' % self.price

# main
if __name__ == '__main__':
    title = raw_input().strip()
    author = raw_input().strip()
    price = int(raw_input().strip())
    new_novel = MyBook(title, author, price)
    new_novel.display()
