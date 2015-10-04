import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int lines = scanner.nextInt();
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>(lines);
        
        // fill the matrix
        for (int i=0; i<lines; i++) {
            int d = scanner.nextInt(); // length of this line list
            matrix.add(i, new ArrayList<Integer>(d));
            for (int j=0; j<d; j++) {
                matrix.get(i).add(scanner.nextInt());
            }
        }
        
        int tests = scanner.nextInt();
        while (tests-- > 0) {
            int x = scanner.nextInt()-1;
            int y = scanner.nextInt()-1;
            
            if (x < lines && y < matrix.get(x).size())
                System.out.println(matrix.get(x).get(y));
            else
                System.out.println("ERROR!");
        }
    }
}
