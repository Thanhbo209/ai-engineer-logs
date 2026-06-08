"""
Phase 1 - Computer Science Foundations Snippets

This file contains small examples for:
- arrays
- hash maps
- searching
- sorting
- recursion
- trees
- graphs
"""

# =========================
# Arrays / Lists
# =========================

nums = [10, 20, 30, 40]

# Access first element: O(1)
print("First element: ", nums[0])

# Add element to the end of the array: amortized O(1)
nums.append(50)
print("After appended: ", nums)

# Insert to index: O(n)
nums.insert(2, 15)
print("After inserted to index 2: ", nums)

# Remove element: O(n)
nums.remove(15)
print("After removed: ", nums)

# =========================
# Hash Map / Dict
# =========================

user = {
    "name": "Thanh",
    "role": "AI Engineer learner",
}

# Access value through key: average O(1)
print(user["name"])

user["level"] = "beginner"
print(user)

# =========================
# Linear Search O(n)
# =========================

def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

print("At index: ", linear_search([10, 20, 30], 30))
print("At index: ", linear_search([10, 20, 30], 99))

# =========================
# Binary Search
# =========================

def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        
        if items[mid] < target:
            right = mid + 1 
        else: 
            left = mid - 1
    return -1

print(binary_search([10, 20, 30, 40, 50], 40))
print(binary_search([10, 20, 30, 40, 50], 99))

# =========================
# Selection Sort
# =========================

def selection_sort(items):
    items = items[:] # Creates a copy so we don't modify the original list

    for i in range(len(items)):
        # Assume the first unsorted element is the minimum
        min_index = i

        for j in range(i + 1, len(items)):
            if items[i] < items[min_index]:
                min_index = j
        
        # Swap the found minimum with the first unsorted element
        items[i], items[min_index] = items[min_index], items[i]

    return items

print(selection_sort([5, 3, 8, 1, 2]))

# =========================
# Recursion
# =========================

def factorical(n):
    if n == 0:
        return 1
    return n * factorical(n - 1)

print(factorical(5))

# =========================
# Tree
# =========================

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_tree(node):
    print(node.value)

    for child in node.children:
        dfs_tree(child)

root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

root.children.append(b)
root.children.append(c)
b.children.append(d)

dfs_tree(root)

# =========================
# Graph
# =========================

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"],
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)


bfs(graph, "A")
