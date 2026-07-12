### Data structures and algorithm exercises
## Overview of Included ImplementationsTwo Sum (two_sum.py)

## Python Implementations
# Concept: Arrays & Hashing. (two_sum.py)
# Approach: Uses a hash map (Python dictionary) to track complement values in a single pass.
# Complexity: $O(n)$ time and $O(n)$ space.Reverse a Linked List (reverse_linked_list.py)

# Concept: Linked Lists. (reverse_linked_list.py)
# Approach: Iterative pointer manipulation using prev, current, and next_node tracking variables.
# Complexity: $O(n)$ time and $O(1)$ space.Valid Parentheses (valid_parentheses.py)

# Concept: Stacks. (valid_parentheses.py)
# Approach: Uses a list as a Last-In-First-Out (LIFO) stack to cleanly push opening brackets and pop/verify matches against a mapping dictionary.
# Complexity: $O(n)$ time and $O(n)$ space.Binary Search (binary_search.py)

# Concept: Searching / Divide and Conquer. (binary_search.py)
# Approach: Iteratively divides the sorted array search space in half using two pointers (low and high).
# Complexity: $O(\log n)$ time and $O(1)$ space.Merge Intervals (merge_intervals.py)

# Concept: Interval Manipulation / Sorting. (merge_intervals.py)
# Approach: Sorts intervals based on the start index, then checks for overlapping boundaries sequentially.
# Complexity: $O(n \log n)$ time and $O(n)$ space.


## Javascript Implementations
# Concept: Arrays & Hashing. (two_sum.js):
# Approach: Using ES6 Map objects to preserve key-value lookups and avoid prototype collision.

# Concept: Reverse a Linked List (reverse_linked_list.js):
# Approach: Standard ES6 class syntax for the ListNode and explicit null checks due to JavaScript's lack of a native LinkedList.

# Concept: Valid Parentheses (valid_parentheses.js):
# Approach: Standard array methods push() and pop() to treat a JavaScript array naturally as a LIFO stack.

# Concept: Binary Search (binary_search.js):
# Approach: Uses Math.floor() during pointer division since JavaScript's division / operator uses floating-point numbers.

Merge Intervals (merge_intervals.js):
# Approach: Custom sorting comparator function (a, b) => a[0] - b[0] since JavaScript's native .sort() converts numbers to strings and sorts lexicographically.
