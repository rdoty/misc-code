import java.util.*;

/* 2019.04.30 Call w/Annie Shin of Nova Credit (45 minutes for exercise)
 * to execute: "javac nc_exercise1.java" "java Solution"
 *
 * Original prompt for exercise below:
 * API to count the number of visitors to our website in the past 1 minute
 * const logHit = () => {
 *   log a visit to the website
 * };

 * const getHits = () => {
 *  returns the number of visits in the past 1 minute
 * };
 */
class Solution {
    private static ArrayList<Long> hitsEachSecond = new ArrayList<Long>();  // Could use something other than ArrayList

    public static void main(String[] args) throws InterruptedException {
        initializeMinuteCounter();
        runDemo();
    }

    /**
     * Add 1 to the last array entry
     */
    private static void logHit() {
        Long hitsThisSecond = Solution.hitsEachSecond.get(Solution.hitsEachSecond.size() - 1);
        Solution.hitsEachSecond.set(Solution.hitsEachSecond.size() - 1, hitsThisSecond + 1);
    }

    /**
     * Adds the values in the entire array
     * @return the total value of the entries in the array
     */
    private static Long getHits() {
        return Solution.hitsEachSecond.stream().mapToLong(a -> a).sum();
    }

    /**
     * This is all the plumbing for the actual business logic of keeping the last 60
     * seconds of hits. Includes some debug output for each second tracked.
     * @throws InterruptedException
     */
    private static void initializeMinuteCounter() throws InterruptedException {
        Solution.hitsEachSecond.add(0L);  // Add a zeroed entry at the end of the list (first entry of the list)

        Timer hitCounterLimiter = new Timer();
        hitCounterLimiter.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that fires every second and truncates the array to
             * the last 59 items then appends a new entry for the current second.
             */
            @Override
            public void run() {
                int firstEntry = Solution.hitsEachSecond.size() > 59 ? Solution.hitsEachSecond.size() - 59 : 0;
                Solution.hitsEachSecond = new ArrayList<Long>(Solution.hitsEachSecond.subList(firstEntry, Solution.hitsEachSecond.size()));
                Solution.hitsEachSecond.add(0L);  // Add a new zeroed entry to the end of the list
                System.out.print(".");  // Debug info indicating a new second has been created
            }
        }, 0,1000);
    }

    /**
     * This is here just for demonstrating the functionality, not really part of the solution.
     * It will run forever until cancelled on the command line.
     */
    private static void runDemo() throws InterruptedException {
        Timer hitLogger = new Timer();
        Timer hitChecker = new Timer();

        hitLogger.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that simulates traffic by firing every
             * half second and logging a hit.
             */
            @Override
            public void run() {
                logHit();
                System.out.print("H");  // Debug info indicating a new hit has been logged
            }
        }, 500, 340);

        hitChecker.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that outputs the numbers of hits periodically
             */
            @Override
            public void run() {
                System.out.println("\ngetHits returns: " + Solution.getHits());
                System.out.println("Seconds logged: " + Solution.hitsEachSecond.size());  // Debug info for # seconds recorded
            }
        }, 10000, 10000);
    }
}


/* This is the original (crappy, broken) attempt in ~40 minutes
import java.util.concurrent.TimeUnit;

class AbortedSolution {
  public static Integer numberOfHits = 0;
  public static ArrayList<Long> timestamp = new ArrayList<Long>();

  public static void main(String[] args) throws InterruptedException {
    ArrayList<String> strings = new ArrayList<String>();
    strings.add("Hello, World!");

    for (String string : strings) {
      System.out.println(string);
    }
    logHits();
    logHits();
    TimeUnit.SECONDS.sleep(60);

    logHits();
    logHits();
    logHits();
    logHits();
    System.out.println(getHits());
  }

  public static void logHits() {
    timestamp.add(System.currentTimeMillis()/1000);
  }

  public static int getHits() {
    Long currenttime = System.currentTimeMillis()/1000;

    for (int i = 0; i < Solution.timestamp.size(); i++) {
      Long time = Solution.timestamp.get(i);
      if (time < (currenttime - 60)) {  // This item is too old to be counted
         // Remove the item from the list
         Solution.timestamp.remove(i);
      }
    }
    return Solution.timestamp.size();
    // return Solution.numberOfHits;
  }
}
*/