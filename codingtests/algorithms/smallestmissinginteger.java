// From https://app.codility.com/demo/results/demoMWUUJC-GWW/
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

// 2019.01.16 Here testing for TopTal

import java.util.Arrays;

class Solution {
    public static int solution(int[] A) {
        // write your code in Java SE 8

        // Count up from one and check the array provided until we
        // don't find our value in the array

        // Sort the array so we don't have to go to the end
        Arrays.sort(A);
        int retVal = 1;
        boolean found = true;
        while (found == true) {
            for (int x : A) {
                if (x == retVal) {
                    retVal++;
                }
            }
            found = false;
        }
        return retVal;
    }

    private static int betterSolution(int[] A) {
        Arrays.sort(A);

        int missingInt = 0;
        for (int entry : A) {
            missingInt += 1;
            if (entry != missingInt) {
                return missingInt;
            }
        }
        return 0;  // Indicates no missing integer
    }

    public static void main(String[] args) {
        runTests();
    }

    private static void runTests() {
        System.out.println(solution(new int[] {1, 2, 4, 6, 3}));  // Expects 5
        System.out.println(solution(new int[] {1, 3, 5, 7, 9}));  // Expects 2
        System.out.println(solution(new int[] {-1, -2, -3, -5})); // Expects 1
        System.out.println(solution(new int[] {1, 2, 3, 4, 5}));  // Expects 6
        System.out.println(solution(new int[] {5, 4, 3, 1, 2}));  // Expects 6

        System.out.println(betterSolution(new int[] {1, 2, 4, 6, 3}));  // Expects 5
        System.out.println(betterSolution(new int[] {1, 3, 5, 7, 9}));  // Expects 2
        System.out.println(betterSolution(new int[] {-1, -2, -3, -5})); // Expects 1
        System.out.println(betterSolution(new int[] {1, 2, 3, 4, 5}));  // Expects 0
        System.out.println(betterSolution(new int[] {5, 4, 3, 1, 2}));  // Expects 0
    }
}
