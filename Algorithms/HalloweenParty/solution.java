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
            long cuts = scanner.nextLong();
            
            // Half of the cuts will be horizontal
            long horizontal = cuts/2;
            
            // For each vertical cut, you'll get <horizontal> chocolate pieces
            System.out.println(horizontal*(cuts-horizontal));
        }
    }
}
