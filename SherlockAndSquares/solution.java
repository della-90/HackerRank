import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        while (lines-- > 0) {
            long min = scanner.nextLong();
            long max = scanner.nextLong();
            int count = 0;
            for (int i=(int)Math.ceil(Math.sqrt(min)); Math.pow(i, 2)<=max; i++) {
                count++;
            }
            System.out.println(count);
        }
        
    }
}
