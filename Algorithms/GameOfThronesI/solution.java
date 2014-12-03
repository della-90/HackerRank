import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner myScan = new Scanner(System.in);
        String inputString = myScan.nextLine();
       
        String ans;
        // Assign ans a value of YES or NO, depending on whether or not inputString satisfies the required condition
        
        /*
         * Una stringa e' palindroma se non esistono 2 o piu' caratteri ripetuti un numero dispari di volte
         */ 
        int[] count = new int[26];
        char[] chars = inputString.toCharArray();
        for (int i=0; i<chars.length; i++) {
            count[chars[i]-'a']++;
        }
        
        int odd = 0;
        ans = "YES";
        for (int i=0; i<count.length; i++) {
            if (count[i] % 2 != 0) {
                if (++odd > 1) {
                    ans = "NO";
                    break;
                }
            }
        }
        
        System.out.println(ans);
        myScan.close();
    }
    
}

