import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        //Read \n
        s.nextLine();
        char[][] map = new char[n][n];
        for (int i=0; i<n; i++) {
            char[] chars = s.nextLine().toCharArray();
            for (int j=0; j<n; j++) {
                map[i][j] = chars[j];
            }
        }
        
        for (int i=1; i<n-1; i++) {
            for (int j=1; j<n-1; j++) {
                if (isCavity(map, i, j)) {
                    map[i][j] = 'X';
                }
            }
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                System.out.print(map[i][j]);
            }
            System.out.println();
        }
        
    }
    
    private static boolean isCavity(char[][] map, int i, int j) {
        boolean result = map[i-1][j] < map[i][j] && // Check north
            map[i+1][j] < map[i][j] && // Check south
            map[i][j-1] < map[i][j] && // Check west
            map[i][j+1] < map[i][j]; // Check east
        return result;
    }
}
