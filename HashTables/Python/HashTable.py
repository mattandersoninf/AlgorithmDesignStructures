class HashTable:
    def __init__(self, size):
        # Initialize the hash table with a given size
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Hashes the key and returns the hash value
        return hash(key) % self.size

    def insert(self, key, value):
        # Inserts a key-value pair into the hash table
        hash_value = self._hash(key)
        slot = self.table[hash_value]
        for pair in slot:
            if pair[0] == key:
                # If key already exists, update the value
                pair[1] = value
                return
        # If key doesn't exist, append the new pair to the slot
        slot.append((key, value))

    def get(self, key):
        # Retrieves the value associated with a given key
        hash_value = self._hash(key)
        slot = self.table[hash_value]
        for pair in slot:
            if pair[0] == key:
                # Return the value if key is found
                return pair[1]
        # Raise KeyError if key is not found
        raise KeyError("Key not found")

    def remove(self, key):
        # Removes a key-value pair from the hash table
        hash_value = self._hash(key)
        slot = self.table[hash_value]
        for i, pair in enumerate(slot):
            if pair[0] == key:
                # Remove the pair if key is found
                del slot[i]
                return
        # Raise KeyError if key is not found
        raise KeyError("Key not found")
    
"""

# Create a hash table of size 10
hash_table = HashTable(10)

# Insert key-value pairs
hash_table.insert("apple", 5)
hash_table.insert("banana", 2)
hash_table.insert("orange", 8)

# Retrieve values
print(hash_table.get("apple"))  # Output: 5
print(hash_table.get("banana"))  # Output: 2
print(hash_table.get("orange"))  # Output: 8

# Update a value
hash_table.insert("apple", 10)
print(hash_table.get("apple"))  # Output: 10

# Remove a key-value pair
hash_table.remove("banana")
print(hash_table.get("banana"))  # Raises KeyError: 'banana' not found

"""