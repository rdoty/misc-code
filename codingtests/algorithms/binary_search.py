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

# Usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_int = 7
    index = binary_search(sorted_list, target_int)
    print(f"sorted_list: {sorted_list}")
    print(f"(Zero-based) Location of target_value {target_int}: {index}")
