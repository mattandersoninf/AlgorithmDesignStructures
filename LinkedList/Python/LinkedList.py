class Node:
    def __init__(self, data):
        self.data = data  # Data value stored in the node
        self.next = None  # Reference to the next node in the linked list

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the linked list is empty, set the new node as the head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Traverse to the end of the linked list and add the new node

    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head
        self.head = new_node  # Set the new node as the head, shifting the current head to the next position

    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next  # If the data to be deleted is in the head node, update the head
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # If the data to be deleted is in a non-head node, adjust the references
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the data value of the current node
            current = current.next
        print("None")
"""
# Test Cases


# Create a new linked list
linked_list = LinkedList()

# Append some elements
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Prepend an element
linked_list.prepend(0)

# Display the linked list
linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Delete an element
linked_list.delete(2)

# Display the linked list after deletion
linked_list.display()  # Output: 0 -> 1 -> 3 -> None

"""