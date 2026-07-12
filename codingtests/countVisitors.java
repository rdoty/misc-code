import java.util.*;
import java.util.stream.IntStream;

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
    private static int[][][][][] hitHistoryArray = new int[3][12][31][24][60];  // Separate experiment

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
        logHitToHistory();
    }

    /**
     * Adds the values in the entire array - represents the last 60 seconds
     * across minute boundaries. Method is really getLastSixtySeconds based
     * on how hitsEachSecond is constructed.
     *
     * @return the total value of the entries in the array
     */
    private static Long getHits() {
        return Solution.hitsEachSecond.stream().mapToLong(a -> a).sum();
    }

    /**
     * This is all the plumbing for the actual business logic of keeping the last 60
     * seconds of hits. Includes some debug output for each second tracked.
     *
     * @throws InterruptedException as an artifact of the timer run loop
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
        }, 0, 1000);
    }

    /**
     * This is here just for demonstrating the functionality, not really part of the solution.
     * It will run forever until cancelled on the command line.
     *
     * @throws InterruptedException as an artifact of the timer run loops
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
                System.out.println("Seconds logged: " + Solution.hitsEachSecond.size());  // Debug info for # seconds recorded
                System.out.println("\ngetHits returns: " + Solution.getHits());
                System.out.println("\ngetHitsThisHour returns: " + getHitsThisHour());
                System.out.println("\ngetHitsThisDate returns: " + getHitsThisDate());
            }
        }, 10000, 10000);
    }

    /**
     * Extend for hits per minute per year:
     * [year][month][day][hour][minute] = #hits
     * [0-x][0-11][0-30][0-23][0-59]
     *
     */
    private static void logHitToHistory() {
        Calendar now = Calendar.getInstance();
        Solution.hitHistoryArray[now.get(Calendar.YEAR)-2019][now.get(Calendar.MONTH)][now.get(Calendar.DATE)][now.get(Calendar.HOUR_OF_DAY)][now.get(Calendar.MINUTE)] += 1;
    }

    public static int getHitsThisHour() {
        Calendar now = Calendar.getInstance();
        return IntStream.of(Solution.hitHistoryArray[now.get(Calendar.YEAR)-2019][now.get(Calendar.MONTH)][now.get(Calendar.DATE)][now.get(Calendar.HOUR_OF_DAY)]).sum();
    }

    public static int getHitsThisDate() {
        Calendar now = Calendar.getInstance();
        int sum = 0;
        for (int hour = 0; hour < 24; hour++) {
            sum += IntStream.of(Solution.hitHistoryArray[now.get(Calendar.YEAR)-2019][now.get(Calendar.MONTH)][now.get(Calendar.DATE)][hour]).sum();
        }
        return sum;
    }

    public static int getHitsThisMonth() {
        Calendar now = Calendar.getInstance();
        int sum = 0;
        for (int date = 0; date < 31; date++) {
            for (int hour = 0; hour < 24; hour++) {
                sum += IntStream.of(Solution.hitHistoryArray[now.get(Calendar.YEAR)-2019][now.get(Calendar.MONTH)][date][hour]).sum();
            }
        }
        return sum;
    }

    public static int getHitsThisYear() {
        Calendar now = Calendar.getInstance();
        int sum = 0;
        for (int month = 0; month < 12; month++) {
            for (int date = 0; date < 31; date++) {
                for (int hour = 0; hour < 24; hour++) {
                    sum += IntStream.of(Solution.hitHistoryArray[now.get(Calendar.YEAR) - 2019][month][date][hour]).sum();
                }
            }
        }
        return sum;
    }

    /**
     * Return a value based one date info passed in
     * @param year
     * @param month
     * @param date
     * @param hour
     * @return
     */
    public static int getHitsFor(int year, int month, int date, int hour) {
        // TODO logic for null month/date/hour values to return sums for year/month/date

        // if all params != null
        return IntStream.of(Solution.hitHistoryArray[year-2019][month][date][hour]).sum();
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