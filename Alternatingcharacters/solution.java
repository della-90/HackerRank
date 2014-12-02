mport java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        // Get rid of \n
        scanner.nextLine();
        for(int l=0; l<lines; l++) {
            char[] chars = scanner.nextLine().toCharArray();
            int length = chars.length;
            int response = 0;
            
            for (int i=0; i<length-1; i++) {
                if (chars[i] == chars[i+1])
                    response++;
            }
            System.out.println(response);
        }
    }
  
}
