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

# Usage
if __name__ == "__main__":
    input_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result_list = merge_intervals(input_intervals)
    print(f"Original Intervals: {input_intervals}")
    print(f"Merged Intervals:   {result_list}")
