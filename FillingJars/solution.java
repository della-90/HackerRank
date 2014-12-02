import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long jars = scanner.nextLong();
        long lines = scanner.nextLong();
        long tot = 0;
        while (lines-- > 0) {
            long low = scanner.nextLong();
            long high = scanner.nextLong();
            long candies = scanner.nextLong();
            
            tot += (candies*(high-low+1)); // high-low+1, because indices are inclusive
        }
        
        System.out.println((long)Math.floor(tot/jars));
    }
}
