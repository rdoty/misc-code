
/**
 * 2019.05.22 Tech call w/Tim @ Amazon
 * Goal: Determine if there is a single value from each set, that, when summed
 * with a single value of the other sets is zero
 *
 * should return false:
 * [0, 1, 1, 1], [1, 2, 2, 2], [2, 3, 3, 3]
 *
 * should return true:
 * [1, 9, 9], [9, -2, 9], [9, 9, 1]
 *
 * Sum any one value from each set to get zero
 */
class SumOfZeroExists {

    private static boolean sumOfZeroExists(int[] arrayA, int[] arrayB, int[] arrayC) {
        // When an array is empty, use an array with a single zero value
        int[] aNotEmpty = arrayA.length > 0 ? arrayA : new int[] { 0 };
        int[] bNotEmpty = arrayB.length > 0 ? arrayB : new int[] { 0 };
        int[] cNotEmpty = arrayC.length > 0 ? arrayC : new int[] { 0 };

        for (int indexA = 0; indexA < aNotEmpty.length; indexA++) {
            for (int indexB = 0; indexB < bNotEmpty.length; indexB++) {
                for (int indexC = 0; indexC < cNotEmpty.length; indexC++) {
                    if (cNotEmpty[indexC] + bNotEmpty[indexB] + aNotEmpty[indexA] == 0) {
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
        var demoPassingInput1 = new int[] { 1, 9, 9 };
        var demoPassingInput2 = new int[] { 9, -2, 9 };
        var demoPassingInput3 = new int[] { 9, 9, 1 };

        var demoFailingInput1 = new int[] { 0, 1, 1, 1 };
        var demoFailingInput2 = new int[] { 1, 2, 2, 2 };
        var demoFailingInput3 = new int[] { 2, 3, 3, 3 };

        var sequence1 = new int[] { 1, 2, 4, 6, 3 };
        var negativeSequence1 = new int[] { -1, -2, -4, -6, -3 };
        var singleElement = new int[] { 5 };
        var emptyArray = new int[] {};

        System.out.println("Demo test results:");
        System.out.println(sumOfZeroExists(demoPassingInput1, demoPassingInput2, demoPassingInput3));
        System.out.println(sumOfZeroExists(demoFailingInput1, demoFailingInput2, demoFailingInput3));

        System.out.println("\nOther test results:");
        System.out.println(sumOfZeroExists(sequence1, emptyArray, emptyArray));
        System.out.println(sumOfZeroExists(sequence1, negativeSequence1, emptyArray));
        System.out.println(sumOfZeroExists(sequence1, negativeSequence1, singleElement));
        System.out.println(sumOfZeroExists(sequence1, singleElement, emptyArray));
    }

}
