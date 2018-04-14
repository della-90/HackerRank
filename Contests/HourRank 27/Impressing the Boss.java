import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the canModify function below.
     */
    static String canModify(int[] a) {
        int[] b = new int[a.length];
        System.arraycopy(a, 0, b, 0, a.length);
        boolean alreadySorted = true;
        for (int i=1; i < a.length; i++) {
            if (a[i] < a[i-1]) {
                a[i] = a[i-1];
                b[i-1] = b[i];
                alreadySorted = false;
                break;
            }            
        }
        
        if (alreadySorted || isSorted(a) || isSorted(b)) {
            return "YES";
        }
        return "NO";
    }
    
    private static boolean isSorted(int[] a) {
        for (int i=1; i<a.length; i++) {
            if (a[i] < a[i-1]) {
                return false;
            }
        }
        
        return true;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int t = scanner.nextInt();
        scanner.skip("\\s*");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("\\s*");

            int[] a = new int[n];

            String[] aItems = scanner.nextLine().split(" ");
            scanner.skip("\\s*");

            for (int aItr = 0; aItr < n; aItr++) {
                int aItem = Integer.parseInt(aItems[aItr]);
                a[aItr] = aItem;
            }

            String result = canModify(a);
            
            System.out.println(result);
        }
        
        scanner.close();
    }
}
