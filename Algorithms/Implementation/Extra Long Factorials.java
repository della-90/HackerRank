import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(factorial(n, BigInteger.ONE));
    }
    
    private static BigInteger factorial(int n, BigInteger result) {
        if (n == 1) {
            return result;
        }
        
        return factorial(n-1, result.multiply(new BigInteger(Integer.toString(n))));
    }
}
