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
public boolean sumOfZeroExists(int[]a,int[]b,int[]c) {
    for (int i=0; i < a.length; i++) {
        for (int j=0; j < b.length; j++) {
            for (int k=0; k < c.length; k++) {
                if (c[k] + b[j] + a[i]==0) {
                    return true;
                }
            }
        }
    }
    return false;
}
