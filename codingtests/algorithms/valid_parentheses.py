def is_valid(s: str) -> bool:
    """
    Given string 's' containing characters '(', ')', '{', '}', '[' and ']',
    determine if input is valid.

    Time Complexity: O(n) - Single pass through string of length n.
    Space Complexity: O(n) - Worst case, stack will hold all brackets.
    """
    stack = []
    # Mapping closing brackets to corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in bracket_map:
            # Pop top element if stack not empty, else assign dummy value
            top_element = stack.pop() if stack else '#'

            # If mapping doesn't match popped element, invalid
            if bracket_map[char] != top_element:
                return False
        else:  # Opening bracket, push onto stack
            stack.append(char)

    return len(stack) == 0  # If stack empty, all brackets properly matched

# Usage
if __name__ == "__main__":
    test_strings = ["()[]{}", "(]", "([)]", "{[]}"]
    for s in test_strings:
        print(f"Is '{s}' valid? {is_valid(s)}")
