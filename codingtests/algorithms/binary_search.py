def binary_search(arr, target):
    """
    With sorted list 'arr', find the index of 'target'. Returns -1 if target not present.

    Time Complexity: O(log n) - Halves the search space each iteration.
    Space Complexity: O(1) - Iterative approach uses constant space.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Usage
if __name__ == "__main__":
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target_val = 7
    index = binary_search(sorted_arr, target_val)
    print(f"Array: {sorted_arr}")
    print(f"Target {target_val} found at index: {index}")
