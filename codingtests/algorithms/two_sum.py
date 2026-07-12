def two_sum(nums, target):
    """
    Given an array of integers 'nums' and an integer 'target', 
    return indices of the two numbers such that they add up to 'target'.
    
    Time Complexity: O(n) - Single pass through the list using a hash map.
    Space Complexity: O(n) - To store up to n elements in the hash map.
    """
    # Map to store the value and its corresponding index
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
        
    return []  # Return empty list if no solution is found

# Example Usage
if __name__ == "__main__":
    example_nums = [2, 7, 11, 15]
    example_target = 9
    result = two_sum(example_nums, example_target)
    print(f"Two Sum Solution for {example_nums} with target {example_target}: {result}")
