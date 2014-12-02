mport java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        scanner.nextLine();
        while (lines -- > 0) {
            char[] chars = scanner.nextLine().toCharArray();
            int result = 0;
            for (int i=0, j=chars.length-1; i<chars.length/2; i++, j--) {
                result += Math.abs(chars[i]-chars[j]);
            }
            
            System.out.println(result);
            
        }
    }
}
