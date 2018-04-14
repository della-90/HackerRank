import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
    
    static void fill(TreeSet<Integer> set, int[] p, int start, int end) {
        for (int i=start; i<end; i++) {
            set.add(p[i]);
        }
    }

    /*
     * Complete the maximumProfit function below.
     */
    static long maximumProfit(int[] p) {
        int[] occurrences = new int[2_000_000];
        for (int i=1; i<p.length; i++) {
            occurrences[p[i]+1_000_000]++;
        }
        OptionalLong result = OptionalLong.empty();
        
        TreeSet<Integer> left = new TreeSet<>();
        TreeSet<Integer> right = new TreeSet<>();
        fill(right, p, 1, p.length);
        for (int i = 1; i<p.length-1; i++) {
            int middle = p[i];
            if (occurrences[middle+1_000_000] == 1) {
                right.remove(middle);
            }
            occurrences[middle+1_000_000]--;

            left.add(p[i-1]);
            if (right.isEmpty()) {
                System.out.println("Empty");
                break;
            }
            left.add(p[i-1]);
            
            Integer a;
            Integer c;
            if (left.size() == 1) {
                a = left.first();
                if (a >= middle) {
                    continue;
                }
                
                if (Integer.signum(middle) == Integer.signum(a)) {
                    c = right.last();
                } else {
                    c = right.higher(middle);
                }
                
                if (c == null || c <= middle) {
                    continue;
                }
            } else {
                c = right.last();

                if (c == null || c <= middle)
                    continue;

                if (Integer.signum(middle) == Integer.signum(c)) {
                    a = left.lower(middle);
                } else {
                    a = left.first();
                }

                if (a == null || a >= middle)
                    continue;
            }
            
            if (result.isPresent()) {
                result = OptionalLong.of(Math.max(result.getAsLong(), 1L*a*middle*c));
            } else {
                result = OptionalLong.of(1L*a*middle*c);
            }
            
        }
        
        return result.orElse(-1);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(scanner.nextLine().trim());

        int[] p = new int[n];

        String[] pItems = scanner.nextLine().split(" ");

        for (int pItr = 0; pItr < n; pItr++) {
            int pItem = Integer.parseInt(pItems[pItr].trim());
            p[pItr] = pItem;
        }

        long result = maximumProfit(p);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
