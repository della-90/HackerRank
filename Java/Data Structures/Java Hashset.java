import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Set<String> set = new HashSet<>();
        
        int n = scanner.nextInt();
        // get rid of newline char after the number
        scanner.nextLine();
        while (n-- > 0) {
            String line = scanner.nextLine();
            set.add(line);
            System.out.println(set.size());
        }
        
    }
}
