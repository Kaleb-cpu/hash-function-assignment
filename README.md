# Hash Function Implementation

This project implements a simple hash function in Python, with collision handling, salting, and additional cryptographic features.

## Features

1. **Simple Hash Function**: Computes a hash value between 0 and 9 based on the sum of ASCII values of the key.
2. **Collision Handling**: Uses chaining (linked lists) to resolve hash collisions.
3. **Salting**: Implements salting to generate a secure 64-bit hash output.
4. **Testing**: Hashes a list of keys and handles collisions with chained nodes.

## Setup

### 1. Clone the repository

Clone the project to your local machine:

```bash
git clone <repo-url>
cd <project-directory>
