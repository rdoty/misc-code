/**
 * Given sorted list 'sortedArray', find the index of 'targetInteger'.
 * Returns -1 if the targetInteger is not present.
 * Time Complexity: O(log n) - Halves the search space in each iteration.
 * Space Complexity: O(1) - Iterative approach uses constant space.
 */
function binarySearch(sortedArray, targetInteger) {
    let rangeStart = 0;
    let rangeEnd = sortedArray.length - 1;

    while (rangeStart <= rangeEnd) {
        let currentLocation = Math.floor((rangeStart + rangeEnd) / 2); // ensure integer division

        if (sortedArray[currentLocation] === targetInteger) {
            return currentLocation;
        } else if (sortedArray[currentLocation] < targetInteger) {
            rangeStart = currentLocation + 1;
        } else {
            rangeEnd = currentLocation - 1;
        }
    }
    return -1;
}

// Usage
const sortedArray = [1, 3, 5, 7, 9, 11, 13, 15];
const targetInteger = 7;
const index = binarySearch(sortedArray, targetInteger);
console.log(`sortedArray: [${sortedArray}]`);
console.log(`(Zero-based) Location of targetValue ${targetInteger}:`, index);
