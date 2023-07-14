class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store the stack elements

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty by comparing the length of the list to zero

    def push(self, item):
        self.stack.append(item)  # Add an item to the top of the stack by appending it to the list

    def pop(self):
        if self.is_empty():  # Check if the stack is empty
            return "Stack is empty"  # Return a message if the stack is empty
        else:
            return self.stack.pop()  # Remove and return the item at the top of the stack using the pop() method

    def peek(self):
        if self.is_empty():  # Check if the stack is empty
            return "Stack is empty"  # Return a message if the stack is empty
        else:
            return self.stack[-1]  # Return the item at the top of the stack without removing it

    def size(self):
        return len(self.stack)  # Return the number of items in the stack by getting the length of the list
    
    
"""
Test Cases

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20

print(stack.is_empty())  # Output: False

print(stack.size())  # Output: 1

"""