# Day 18: Queues and Stacks

# Palindromes:
# It is a word, phrase, number, or other sequence of characters which
# reads the same backwards and forwards.
import Queue

# Determine if a word is a palindrome
class Solution():
    """Determine if a word is a palindrome."""
    def __init__(self):
        """Initialize object with a given stack or queue."""
        self.stack = []
        self.queue = Queue.Queue()

    # Push item at the top(end) of stack(list)
    def pushCharacter(self, char):
        """Pushes a character onto a stack."""
        self.stack.append(char)

    # Removes and returns the item at top(end) in stack(list)
    def popCharacter(self):
        """Pops and returns the character at the top of the stack."""
        return self.stack.pop()

    # Add item to the end(back) of queue(queue)
    def enqueueCharacter(self, char):
        """Enqueues a character in the queue."""
        self.queue.put(char)

    # Removes and returns the first item in the queue(queue)
    def dequeueCharacter(self):
        """Dequeues and returns the first character in the queue."""
        try:
            return self.queue.get()
        except Exception:
            return None


# main
if __name__ == '__main__':
    word = raw_input()
    obj = Solution()
    length = len(word)

    # push/enqueue all the characters of the string s
    for i in range(length):
        obj.pushCharacter(word[i])
        obj.enqueueCharacter(word[i])

    isPalindrome = True
    '''
    pop the top character from stack,
    dequeue the first character, and
    compare both characters
    '''
    for i in range(length / 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome = False
            break

    # Print result string
    message = "The word, %s, " % word
    if isPalindrome:
        print message + "is a palindrome."
    else:
        print message + "is not a palindrome."
