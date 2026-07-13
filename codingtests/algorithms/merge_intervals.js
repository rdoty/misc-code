/**
 * Given array of intervals where intervalArray[i] = [start_i, end_i],
 * merge all overlapping intervals, return array of non-overlapping intervals.
 * Time Complexity: O(n log n) - Sorting the intervals takes O(n log n) time.
 * Space Complexity: O(n) or O(log n) depending on the sorting implementation.
 */
function mergeIntervalArray(intervalArray) {
    if (intervalArray.length === 0) {
        return [];
    }

    intervalArray.sort((a, b) => a[0] - b[0]);  // Sort on starting values

    const mergedArray = [intervalArray[0]];
    for (let i = 1; i < intervalArray.length; i++) {
        let current = intervalArray[i];
        let lastMergedArray = mergedArray[mergedArray.length - 1];

        if (current[0] <= lastMergedArray[1]) {  // if interval overlaps, merge
            lastMergedArray[1] = Math.max(lastMergedArray[1], current[1]);
        } else {
            mergedArray.push(current);
        }
    }
    return mergedArray;
}

// Usage
const inputIntervalArray = [[1, 3], [2, 6], [8, 10], [15, 18]];
const resultArray = mergeIntervalArray(inputIntervalArray);
console.log("Original Intervals:", JSON.stringify(inputIntervalArray));
console.log("mergedArray Intervals:  ", JSON.stringify(resultArray));
