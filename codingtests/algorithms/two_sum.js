/**
 * Given array of integers 'numArray' and integer 'target',
 * return array of indices of two numbers that add up to 'target'.
 * Time Complexity: O(n) - Single pass through the array via Map.
 * Space Complexity: O(n) - Store up to n elements in the Map.
 */
function twoSum(numArray, target) {
    const seen = new Map();
    for (let i = 0; i < numArray.length; i++) {
        const complement = target - numArray[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(numArray[i], i);
    }
    return []; // Return empty if no solution found
}

// Usage
const inputNumArray = [2, 7, 11, 15];
const inputTarget = 9;
const resultArray = twoSum(inputNumArray, inputTarget);
console.log(`Two Sum Solution for [${inputNumArray}] with target ${inputTarget}:`, resultArray);
