
/**
 * 2019.05.22 Tech call w/Tim @ Amazon
 * Goal: Determine if there is a single value from each set, that, when summed
 * with a single value of the other sets is zero
 *
 * false
 * [0, 1, 1, 1]
 * [0, 2, 2, 2]
 * [0, 3, 3, 3]
 * <p>
 * true
 * [1, 9, 9]
 * [9, -2, 9]
 * [9, 9, 1]
 * <p>
 * Sum any one value from each set to get zero
 */
class SumOfZeroExists {

    private static boolean sumOfZeroExists(int[] a, int[] b, int[] c) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b.length; j++) {
                for (int k = 0; k < c.length; k++) {
                    if (c[k] + b[j] + a[i] == 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        runTests();
    }

    private static void runTests() {
        var firstExampleArray = new int[] { 1, 2, 4, 6, 3 };
        var secondExampleArray = new int[] { -1 };
        var thirdExampleArray = new int[] { 5 };
        var emptyArray = new int[] {};

        System.out.println(sumOfZeroExists(firstExampleArray, emptyArray, emptyArray));
        System.out.println(sumOfZeroExists(firstExampleArray, secondExampleArray, emptyArray));
        System.out.println(sumOfZeroExists(firstExampleArray, secondExampleArray, thirdExampleArray));
        System.out.println(sumOfZeroExists(firstExampleArray, thirdExampleArray, emptyArray));
    }

}
