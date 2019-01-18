// From https://app.codility.com/demo/results/demoMWUUJC-GWW/
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

// 2019.01.16 Here testing for TopTal

import java.util.Arrays;

package foo;

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

    public static void main(String[] args) {
        int[] A = {10,20,30,40,50,60,71,80,90,91};;
        System.out.println(solution(A));
        A = new int[] {1,2,3,5,6,7};
        System.out.println(solution(A));
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution;
        int[] A = {10,20,30,40,50,60,71,80,90,91};;
        System.out.println(solution(A));
        A = new int[] {1,2,3,5,6,7};
        System.out.println(solution(A));
    }
}

