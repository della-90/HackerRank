import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++){
            System.out.println(Solve(in.nextInt(), in.nextInt(), in.nextInt()));
        }
    }
    
    private static long Solve(int N, int C, int M){
        long bought = N/C;        
        long wrappersAvailable = bought;
        while (wrappersAvailable >= M) {
            wrappersAvailable -= M;
            wrappersAvailable++; // I've just bought another chocolate
            bought += 1;
        }
        return bought;
    }
    
    
}

