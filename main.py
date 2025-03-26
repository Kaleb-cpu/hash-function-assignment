from hash_table import HashTable

# 1. Implement a Simple Hash Function
def simple_hash(key):
    key_str = str(key)
    ascii_sum = sum(ord(char) for char in key_str)
    hash_value = ascii_sum % 10
    return hash_value

# 2. Hash a List of Keys

keys = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'mango', 'plum']
for key in keys:
    print(f"key: {key}, Hash: {simple_hash(key)}")


# 3.	Observe Collision

'''
After observation ther were collision with these
Hash values
Hash 0 → apple, mango
Hash 6 → orange, kiwi, plum
Hash 9 → banana, melon

There are many ways to handle collisions in hashing
One of them is separate chaining which we will implement
This is how separate chaining works, instead of storing a single
value in an index we would store multiple values, but each value
that is added is chained or linked to the value that was already there, 
thus you end up having a list at that index. 
We will do this using dictionaries.
'''

# 4. Implement Collision Handling

# Create a hash table
hash_table = HashTable()

# Insert keys with their lengths as values
for key in keys:
    hash_table.insert(key, len(key))

# Search for each key
print("\nSearch Results:")
for key in keys:
    value = hash_table.search(key)
    print(f"Key: {key}, Value: {value}")

