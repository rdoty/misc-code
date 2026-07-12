def merge_intervals(intervals):
    """
    Given array of intervals where intervals[i] = [start_i, end_i],
    merge overlapping intervals, return array of non-overlapping intervals.

    Time Complexity: O(n log n) - Sorting intervals takes O(n log n) time.
    Space Complexity: O(n) or O(log n) depending on sorting implementation.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on starting values

    merged = [intervals[0]]

    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        current_start, current_end = current

        if current_start <= prev_end:  # If overlap with previous one, merge
            merged[-1][1] = max(prev_end, current_end)
        else:
            merged.append(current)

    return merged

# Usage
if __name__ == "__main__":
    example_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge_intervals(example_intervals)
    print(f"Original Intervals: {example_intervals}")
    print(f"Merged Intervals:   {result}")
