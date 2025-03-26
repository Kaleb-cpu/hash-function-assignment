from hash_node import Node

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Initialize an empty hash table

    def hash_function(self, key):
        key_str = str(key)  # Convert key to string
        ascii_sum = sum(ord(char) for char in key_str)  # Sum ASCII values
        return ascii_sum % self.size  # Compute hash value

    def insert(self, key, value):
        index = self.hash_function(key)  # Get the hash index
        new_node = Node(key, value)  # Create a new node

        if self.table[index] is None:  # If no collision
            self.table[index] = new_node
        else:  # Collision occurs, use chaining (linked list)
            current = self.table[index]
            while current.next:  # Traverse to the end of the chain
                if current.key == key:
                    current.value = value  # Update value if key already exists
                    return
                current = current.next
            current.next = new_node  # Insert at the end of the list

    def search(self, key):
        index = self.hash_function(key)  # Get the hash index
        current = self.table[index]

        while current:  # Traverse the linked list
            if current.key == key:
                return current.value  # Return the value if found
            current = current.next
        return None  # Return None if key is not found

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            print(f"Index {i}: ", end="")
            while current:
                print(f"({current.key}: {current.value}) -> ", end="")
                current = current.next
            print("None")
