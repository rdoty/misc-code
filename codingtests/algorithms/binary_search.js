/**
 * Given sorted list 'arr', find the index of 'target'.
 * Returns -1 if the target is not present.
 * Time Complexity: O(log n) - Halves the search space in each iteration.
 * Space Complexity: O(1) - Iterative approach uses constant space.
 */
function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2); // ensure integer division

        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

// Usage
const sortedArr = [1, 3, 5, 7, 9, 11, 13, 15];
const targetVal = 7;
const index = binarySearch(sortedArr, targetVal);
console.log(`Array: [${sortedArr}]`);
console.log(`Target ${targetVal} found at index:`, index);
