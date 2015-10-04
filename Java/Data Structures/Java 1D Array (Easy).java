import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] array = new int[n];
        for (int i=0; i<n; i++) {
            array[i] = scanner.nextInt();
        }
        
        int count = 0;
        for (int i=0; i<n; i++) {
            int tmp = 0;
            for (int j=0; j<n-i; j++) {
                tmp += array[i+j];
                
                if (tmp < 0) {
                    count++;
                }
            }
        }
        
        System.out.println(count);
    }
}
