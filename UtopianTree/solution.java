import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        for (int l=0; l<lines; l++) {
            int size = 1;
            int cycles = scanner.nextInt();
            for (int i=0; i<cycles; i++) {
                if (i%2==0) { // spring
                    size *= 2;
                } else { // summer
                    size += 1;
                }
            }
            System.out.println(size);
        }
    }
}
