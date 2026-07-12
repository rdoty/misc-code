/**
 * Given array of integers 'nums' and integer 'target',
 * return indices of two numbers that add up to 'target'.
 * Time Complexity: O(n) - Single pass through the array via Map.
 * Space Complexity: O(n) - To store up to n elements in the Map.
 */
function twoSum(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(nums[i], i);
    }
    return []; // Return empty if no solution found
}

// Usage
const exampleNums = [2, 7, 11, 15];
const exampleTarget = 9;
const result = twoSum(exampleNums, exampleTarget);
console.log(`Two Sum Solution for [${exampleNums}] with target ${exampleTarget}:`, result);
