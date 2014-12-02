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
            int count = 0;
            int n = scanner.nextInt();
            char[] chars = String.valueOf(n).toCharArray();
            for (int j=0; j<chars.length; j++) {
                int digit = Character.getNumericValue(chars[j]);
                if (digit != 0 && n%digit==0) {
                    count++;
                }
            }
            System.out.println(count);
        }
    }
}
