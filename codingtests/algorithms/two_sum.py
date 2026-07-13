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

# Example Usage
if __name__ == "__main__":
    input_num_list = [2, 7, 11, 15]
    input_target_int = 9
    result_list = two_sum(input_num_list, input_target_int)
    print(f"Two Sum Solution for {input_num_list} with target {input_target_int}: {result_list}")
