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
            
            if (deepFirstSearch(array, new HashSet<Integer>(), m, 0))
                System.out.println("YES");
            else
                System.out.println("NO");            
        }
    }
    
    // Main worker. Performs a deep-first search
    public static boolean deepFirstSearch(int[] array, Set<Integer> visited, int m, int current) {
        if (worker(array, visited, m, current, -1))
            return true;
        if (worker(array, visited, m, current, 1))
            return true;
        if (worker(array, visited, m, current, m))
            return true;
        return false;
    }
    
    // generic worker
    private static boolean worker(int[] array, Set<Integer> visited, int m, int current, int move) {
        int nextpos = current + move;
        
        if (nextpos < 0)
            return false;
        
        if (nextpos >= array.length)
            return true;
        
        if (visited.add(nextpos) && array[nextpos] == 0)
            return deepFirstSearch(array, visited, m, nextpos);
        
        return false;
    }
  
}
