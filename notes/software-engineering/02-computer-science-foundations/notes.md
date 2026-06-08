# Computer Science Foundations Notes

## Goal

Understand basic computer science concepts needed to reason about software systems and later AI systems.

## Topics

- Big O Notation
- Arrays / Lists
- Hash maps
- Trees
- Graphs
- Sorting and searching
- Recursion
- Big-O time and space
- Linux CLI basics
- HTTP, REST, JSON
- Client/server model

---

## Big O Notation

Big O is used to describe algorithm efficiency.

- **O(1) is constant time**

- **O(n) scales linearly**

- **O(n^2) is quadratic**

- Time Complexity: How runtime scales with input size. Related to Big O notation.

- Space Complexity: How memory usage scales with input size.

- Constant Time: Algorithms taking the same time regardless of input size. Represented as O(1).

- Linear Time: Run time scales linearly with input size. Represented as O(N).

---

## Arrays / Lists

An array/list stores items in order.

Common operations:

- Access by index: O(1)
- Search by value: O(n)
- Append at end: amortized O(1)
- Insert in middle: O(n)
- Delete from middle: O(n)

Arrays are good when I need ordered data and fast index access.

---

## Hash Maps

A hash map stores key-value pairs.

Common operations:

- Insert: average O(1), worst O(n)
- Lookup: average O(1), worst O(n)
- Delete: average O(1), worst O(n)

Worst case happens when many keys collide into the same bucket.

---

## Searching

Linear search checks each item one by one.

- Works on unsorted data
- Time: O(n)

Binary search cuts the search space in half each step.

- Requires sorted data
- Time: O(log n)

---

## Sorting

Selection sort is simple but slow.

- Time: O(n²)

Python's built-in sort is better for real work.

- Time: O(n log n)

---

## Recursion

Recursion is when a function calls itself.

Every recursive function needs:

1. Base case
2. Recursive case

Without a base case, recursion keeps calling itself until the program crashes.

---

## Trees

A tree is hierarchical data.

Examples:

- File system
- HTML DOM
- Organization chart
- Comment replies

Important terms:

- Root
- Child
- Parent
- Leaf
- Depth

DFS goes deep before wide.

BFS goes level by level.

---

## Graphs

A graph is a set of nodes connected by edges.

Examples:

- Social networks
- Maps
- Web links
- Dependency graphs

A visited set prevents infinite loops when the graph has cycles.

BFS uses a queue.

DFS uses recursion or a stack.

---

## HTTP / JSON / Client Server

A client sends a request.

A server returns a response.

JSON is a common format for sending structured data.

Common status codes:

- 200: OK
- 201: Created
- 400: Bad request
- 401: Unauthorized
- 404: Not found
- 500: Server error
