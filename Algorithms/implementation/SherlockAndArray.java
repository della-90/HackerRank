import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int tests = s.nextInt();
        while ((tests--) > 0) {
            int n = s.nextInt();
            int[] array = new int[n];
            int total = 0;
            for (int i=0; i<n; i++) {
                array[i] = s.nextInt();
                total += array[i];
            }
            if (isSatisfied(array, total)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
    
    private static boolean isSatisfied(int[] array, int total) {
        if (array.length <= 1) {
            return true;
        }
        
        if (array.length == 2) {
            // 0 not allowed
            return false;
        }
        
        int left = 0;
        for (int i=1; i<array.length-1; i++) {
            
            left += array[i-1];
            
            if (left*2 == (total-array[i])) {
                return true;
            }
            
            if (left*2 > (total-array[i])) {
                // no way to get left == right, because left is already > right
                break;
            }
            
        }
        return false;
    }
}
