/**
 * Given array of intervals where intervals[i] = [start_i, end_i],
 * merge all overlapping intervals, return array of non-overlapping intervals.
 * Time Complexity: O(n log n) - Sorting the intervals takes O(n log n) time.
 * Space Complexity: O(n) or O(log n) depending on the sorting implementation.
 */
function mergeIntervals(intervals) {
    if (intervals.length === 0) {
        return [];
    }

    intervals.sort((a, b) => a[0] - b[0]);  // Sort on starting values

    const merged = [intervals[0]];
    for (let i = 1; i < intervals.length; i++) {
        let current = intervals[i];
        let lastMerged = merged[merged.length - 1];

        if (current[0] <= lastMerged[1]) {  // if interval overlaps, merge
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            merged.push(current);
        }
    }
    return merged;
}

// Usage
const exampleIntervals = [[1, 3], [2, 6], [8, 10], [15, 18]];
const result = mergeIntervals(exampleIntervals);
console.log("Original Intervals:", JSON.stringify([[1, 3], [2, 6], [8, 10], [15, 18]]));
console.log("Merged Intervals:  ", JSON.stringify(result));
