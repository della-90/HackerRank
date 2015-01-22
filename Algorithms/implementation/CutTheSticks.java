import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        List<Integer> sticks = new LinkedList<Integer>();
        for (int i=0; i<n; i++) {
            sticks.add(s.nextInt());
        }
        
        // Sort the list
        Collections.sort(sticks);
        
        while(sticks.size() > 0) {
            // Get shortest
            int shortest = sticks.remove(0);
            int count = 1;
            // Remove all shortest elements
            for (ListIterator<Integer> iterator = sticks.listIterator(); iterator.hasNext();) {
                int next = iterator.next() - shortest;
                count++;
                if (next <= 0) {
                    iterator.remove();
                } else {
                    iterator.set(next);
                }
    
            }
            System.out.println(count);
        }
    }
}
