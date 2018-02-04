import java.io.*;
import java.util.*;

public class Solution {

    public static void insertionSort(int[] arr){
        int i, j, newValue;
        int shifts = 0;
        for (i = 1; i < arr.length; i++) {
            newValue = arr[i];
            j = i;
            while (j > 0 && arr[j - 1] > newValue) {
                arr[j] = arr[j - 1];
                shifts++;
                j--;
            }
            arr[j] = newValue;
        }
        
        System.out.println(shifts);

    }
    
    


    static void printArray(int[] ar) {
        for(int n: ar){
            System.out.print(n+" ");
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] ar = new int[n];
        for(int i=0;i<n;i++){
            ar[i]=in.nextInt();
        }
        insertionSort(ar);
    }
}
