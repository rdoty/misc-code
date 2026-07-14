def merge_intervals(interval_list):
    """
    Given array of intervals where interval_list[i] = [start_i, end_i],
    merge overlapping intervals, return array of non-overlapping intervals.

    Time Complexity: O(n log n) - Sorting interval_list takes O(n log n) time.
    Space Complexity: O(n) or O(log n) depending on sorting implementation.
    """
    if not interval_list:
        return []

    interval_list.sort(key=lambda x: x[0])  # Sort intervals based on starting values

    merged_intervals = [interval_list[0]]

    for current in interval_list[1:]:
        prev_start, prev_end = merged_intervals[-1]
        current_start, current_end = current

        if current_start <= prev_end:  # If overlap with previous one, merge
            merged_intervals[-1][1] = max(prev_end, current_end)
        else:
            merged_intervals.append(current)

    return merged_intervals


def test_merge_intervals():
    test_data_list = [
        {
            'input': [[1, 3], [2, 6], [8, 10], [15, 18]], 
            'expected': [[1, 6], [8, 10], [15, 18]]
        },
        {
            'input': [[1, 3], [5, 6], [8, 10], [15, 18]], 
            'expected': [[1, 3], [5, 6], [8, 10], [15, 18]]
        },
        {
            'input': [[1, 3], [2, 6], [5, 10], [9, 18]], 
            'expected': [[1, 18]]
        },
        {'input': [[1,2]], 'expected': [[1,2]]},
        {'input': [[1]], 'expected': [[1]]},
        {'input': [], 'expected': []},
    ]
    for count, test_data in enumerate(test_data_list):
        actual = merge_intervals(test_data['input'])
        assert actual == test_data['expected'], \
            f"Test #{count+1}: Expected {test_data['expected']}, actual: {actual}"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_merge_intervals()  # run tests
