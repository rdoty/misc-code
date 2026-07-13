def is_valid(input_bracket_string: str) -> bool:
    """
    Given string containing characters '(', ')', '{', '}', '[' and ']',
    determine if it is valid.

    Time Complexity: O(n) - Single pass through string of length n.
    Space Complexity: O(n) - Worst case, stack will hold all brackets.
    """
    stack_nested_brackets = []
    # Mapping closing brackets to corresponding opening brackets
    matching_bracket_map = {")": "(", "}": "{", "]": "["}

    for char in input_bracket_string:
        if char in matching_bracket_map:
            # Pop top element if stack not empty, else assign dummy value
            top_element = stack_nested_brackets.pop() if stack_nested_brackets else '#'

            # If mapping doesn't match popped element, invalid
            if matching_bracket_map[char] != top_element:
                return False
        else:  # Opening bracket, push onto stack
            stack_nested_brackets.append(char)

    return len(stack_nested_brackets) == 0  # If stack empty, all brackets properly matched

# Usage
if __name__ == "__main__":
    test_strings = ["()[]{}", "(]", "([)]", "{[]}", "{(([{}]))}"]
    for s in test_strings:
        print(f"'{s}' is {'' if is_valid(s) else 'not '}valid")
