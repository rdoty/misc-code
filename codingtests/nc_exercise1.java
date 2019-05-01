import java.io.*;
import java.util.*;

/* 2019.04.30 Call w/Annie Shin of Nova Credit
 * API to count the number of visitors to our website in the past 1 minute
 * const logHit = () => {
 *   log a visit to the website
 * };

 * const getHits = () => {
 *  returns the number of visits in the past 1 minute
 * };
 */
import java.io.*;
import java.util.*;

class Solution {
    private static ArrayList<Long> hitsPerSecond = new ArrayList<Long>();

    public static void main(String[] args) throws InterruptedException {
        Solution.hitsPerSecond.add(0L);

        Timer hps = new Timer();
        hps.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that fires every second and truncates the array to
             * the last 59 items then appends a new entry for the current second.
             */
            @Override
            public void run() {
                int firstEntry = Solution.hitsPerSecond.size() > 59 ? 1 : 0;
                Solution.hitsPerSecond = new ArrayList<Long>(Solution.hitsPerSecond.subList(firstEntry, Solution.hitsPerSecond.size()));
                Solution.hitsPerSecond.add(0L);
                System.out.print(".");  // Debug info indicating a new second has been created
            }
        }, 0,1000);

        Timer hf = new Timer();
        hf.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that simulates traffic by firing every
             * half second and logging a hit.
             */
            @Override
            public void run() {
                logHits();
            }
        }, 500, 340);

        Timer gh = new Timer();
        gh.scheduleAtFixedRate(new TimerTask() {
            /**
             * This is the method that outputs the numbers of hits periodically
             */
            @Override
            public void run() {
                System.out.println("getHits returns: " + Solution.getHits());
            }
        }, 10000, 10000);

    }

    /**
     * Add 1 to the last array entry
     */
    private static void logHits() {
        Long currentHits = Solution.hitsPerSecond.get(Solution.hitsPerSecond.size() - 1);
        Solution.hitsPerSecond.set(Solution.hitsPerSecond.size() - 1, currentHits + 1);
        System.out.print("H");  // Debug info indicating a new hit has been logged
    }

    /**
     * Adds the values in the entire array
     * @return the total value of the entries in the array
     */
    private static Long getHits() {
        System.out.println("\nSeconds logged: " + Solution.hitsPerSecond.size());
        return Solution.hitsPerSecond.stream().mapToLong(a -> a).sum();
    }
}


/*
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