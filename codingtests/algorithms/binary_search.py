def binary_search(sorted_list, target_int):
    """
    In 'sorted_list', find index of 'target_int'. Returns -1 if target_int not present.

    Time Complexity: O(log n) - Halves the search space each iteration.
    Space Complexity: O(1) - Iterative approach uses constant space.
    """
    range_start = 0
    range_end = len(sorted_list) - 1

    while range_start <= range_end:
        current_location = (range_start + range_end) // 2  # middle of range

        if sorted_list[current_location] == target_int:
            return current_location
        elif sorted_list[current_location] < target_int:
            range_start = current_location + 1
        else:
            range_end = current_location - 1

    return -1


def test_binary_search():
    test_data_list = [
        {'sorted_list': [1, 3, 5, 7, 9], 'search_value': 0, 'expected': -1},
        {'sorted_list': [1, 3, 5, 7, 9], 'search_value': 2, 'expected': -1},
        {'sorted_list': [1, 3, 5, 7, 9], 'search_value': 3, 'expected': 1},
        {'sorted_list': [1, 3, 5, 7, 9], 'search_value': 7, 'expected': 3},
        {'sorted_list': [1, 3, 5, 7, 9], 'search_value': 10, 'expected': -1},
    ]

    for count, test_data in enumerate(test_data_list):
        actual = binary_search(test_data['sorted_list'], test_data['search_value'])
        assert actual == test_data['expected'], \
            f"Test #{count+1}: Expected index of value: '{test_data['search_value']}' to be: '{test_data['expected']}', in list {test_data['sorted_list']}, actual: {actual}"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_binary_search()  #run tests
