class Queue:
    def __init__(self):
        # Initialize an empty list to store the queue elements
        self.items = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item at the front of the queue
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if self.is_empty():
            return None
        return self.items[0]
    
"""

queue = Queue()
print(queue.is_empty())  # True

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.size())  # 3
print(queue.peek())  # "A"

item = queue.dequeue()
print(item)  # "A"
print(queue.size())  # 2
        
"""