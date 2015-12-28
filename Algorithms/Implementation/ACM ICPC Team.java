import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int index = 0;
        int people = scanner.nextInt();
        int topics = scanner.nextInt();
        int[][] matrix = new int[people][topics];
        
        // Acquire data
        while (index < people) {
            String subj = scanner.next();
            for (int i=0; i<subj.length(); i++) {
                char c = subj.charAt(i);
                if (c == '1') {
                    matrix[index][i]++;
                }
            }
            index++;
        }
        
        int maxTopics = 0;
        int teams = 0;
        for (int p1=0; p1<people; p1++) {
            for (int p2=p1+1; p2<people; p2++) {
                int curTopics = 0;
                for (int t=0; t<topics; t++) {
                    if (matrix[p1][t] == 1 || matrix[p2][t] == 1) {
                        curTopics++;
                    }
                }
                
                if (curTopics > maxTopics) {
                    maxTopics = curTopics;
                    teams = 1;
                } else if (curTopics == maxTopics) {
                    teams++;
                }
            }
        }
        
        System.out.println(maxTopics);
        System.out.println(teams);
    }
}