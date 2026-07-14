def two_sum(num_list, target_int):
    """
    Given array of integers 'num_list' and integer 'target_int', 
    return list of indices of the two numbers that add up to 'target_int'.
    
    Time Complexity: O(n) - Single pass through list using hash map.
    Space Complexity: O(n) - Store up to n elements the hash map.
    """
    # Map to store the value and its corresponding location
    seen = {}
    
    for location, value in enumerate(num_list):
        complement = target_int - value
        if complement in seen:
            return [seen[complement], location]
        seen[value] = location
        
    return []  # Return empty list if no solution is found


def test_two_sum():
    test_data_list = [
        {"list": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"list": [2, 7, 11, 15], "target": 18, "expected": [1, 2]},
        {"list": [2, 7, 11, 15], "target": 13, "expected": [0, 2]},
        {"list": [2, 7, 11, 15], "target": 3, "expected": []},
    ]
    for count, test_data in enumerate(test_data_list):
        actual = two_sum(test_data['list'], test_data["target"])
        assert actual == test_data["expected"], \
            f"Test #{count+1}: Expected: {test_data['expected']}, actual: {actual}"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_two_sum()  # run tests
