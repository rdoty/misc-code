def is_valid_nesting(input_bracket_string: str) -> bool:
    """
    Given string containing characters '(', ')', '{', '}', '[' and ']',
    determine if it is valid.

    Time Complexity: O(n) - Single pass through string of length n.
    Space Complexity: O(n) - Worst case, stack will hold all brackets.
    """
    stack_nested_brackets:list = []
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


def test_is_valid_nesting():
    test_data_list = [
        {'input': "()[]{}", 'expected': True}, 
        {'input': "(]", 'expected': False}, 
        {'input': "([)]", 'expected': False}, 
        {'input': "{[]}", 'expected': True}, 
        {'input': "{(([{}]))}", 'expected': True}, 
    ]
    
    for count, test_data in enumerate(test_data_list):
        actual = is_valid_nesting(test_data['input'])
        assert actual == test_data['expected'], \
            f"Test #{count+1}: Expected '{test_data['input']}' to return {test_data['expected']}, actual: {actual}"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_is_valid_nesting()  # run tests
