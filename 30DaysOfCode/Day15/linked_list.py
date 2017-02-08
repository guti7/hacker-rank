# Day 15: Linked List

# Node class is provided.
# A node object is an integer data field, data, and a Node instance pointer,
# nest, pointing to another noce(i.e.: the next node in a list)

# The insert function has two parameters: a pointer, head, pointing to the
# first node of a linked list, and an integer data value that must be added
# to the end of the list as a new Node object.

# Task:
# Complete insert function so it creates a new Node(pass data as the Node
# constructor argument) and insert it at the tail of the linked list
# referenced by the head parameter. Return the reference to the head node.


# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # possibly Node


# Linked List class
class LinkedList:

    def insert(self, head, data):
        if not head:  # empty list
            head = Node(data)  # return Node(data)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)
        return head

    def display(self, head):
        current_node = head
        while current_node:
            print current_node.data,
            current_node = current_node.next

# main
if __name__ == '__main__':
    mylist = LinkedList()
    T = int(input()) # raw_input()
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)
