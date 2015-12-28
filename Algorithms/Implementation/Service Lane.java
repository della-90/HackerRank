import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    private static final int BIKE = 1;
    private static final int CAR = 2;
    private static final int TRUCK = 3;

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int length = s.nextInt();
        int tests = s.nextInt();
        int[] width = new int[length];
        // get width array
        for (int i=0; i<length; i++) {
            width[i] = s.nextInt();
        }
        
        for (int index=0; index<tests; index++) {
            int start = s.nextInt();
            int end = s.nextInt();
            
            int min = width[start];
            for (int i=start+1; i<=end; i++) {
                if (width[i] < min) {
                    min = width[i];
                }
                
                if (min == BIKE) {
                    break;
                }
            }
            
            System.out.println(min);
        }
    }    
}
