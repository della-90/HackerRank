import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tests = scanner.nextInt();
        while (tests-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            
            int[] array = new int[n];
            for (int i=0; i<n; i++) {
                array[i] = scanner.nextInt();
            }
            
            if (worker(array, new HashSet<Integer>(), m, 0))
                System.out.println("YES");
            else
                System.out.println("NO");            
        }
    }
    
    // Main worker. Performs a deep-first search
    public static boolean worker(int[] array, Set<Integer> visited, int m, int current) {
        if (current > 0 && dec(array, visited, m, current))
            return true;
        if (inc(array, visited, m, current))
            return true;
        if (incm(array, visited, m, current))
            return true;
        return false;
    }
    
    // Try to perform an x-1 move
    private static boolean dec(int[] array, Set<Integer> visited, int m, int current) {
        // current must be > 0        
        if (visited.add(current-1) && array[current-1] == 0) {
            return worker(array, visited, m, current-1);
        }
        
        return false;
    }
    
    // Try to perform an x+1 move
    private static boolean inc(int[] array, Set<Integer> visited, int m, int current) {
        int nextpos = current+1;
        if (nextpos >= array.length) {
            return true;
        }
        
        if (visited.add(nextpos) && array[nextpos] == 0)
            return worker(array, visited, m, nextpos);
        
        return false;
    }
    
    // Try to perform an x+m move
    private static boolean incm(int[] array, Set<Integer> visited, int m, int current) {
        int nextpos = current + m;
        // Goal reached
        if (nextpos >= array.length)
            return true;

        // Recursive call
        if (visited.add(nextpos) && array[nextpos] == 0)
            return worker(array, visited, m, nextpos);
        
        // Fail
        return false;
    }
}
