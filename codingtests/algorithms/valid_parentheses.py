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
    test_data_list = [
        {"test_input": "()[]{}", "expected_output": True}, 
        {"test_input": "(]", "expected_output": False}, 
        {"test_input": "([)]", "expected_output": False}, 
        {"test_input": "{[]}", "expected_output": True}, 
        {"test_input": "{(([{}]))}", "expected_output": True}, 
    ]
    
    for test_data in test_data_list:
        actual = is_valid(test_data['test_input'])
        assert actual == test_data['expected_output'], \
            f"Expected '{test_data['test_input']}' to be {test_data['expected_output']}"

    print(f"PASSED {len(test_data_list)} TESTS")
