
import java.util.*;
public class Solution {
       
    static void partition(int[] ar) {
        List<Integer> lower = new LinkedList<Integer>();
        List<Integer> greater = new LinkedList<Integer>();
        int j=0;
        int pivot = ar[0];
        greater.add(pivot);
        for (int i=1; i<ar.length; i++) {
            if (ar[i] < pivot) {
                lower.add(ar[i]);
            } else {
                greater.add(ar[i]);
            }
        }
        
        for (Integer i : lower) {
            System.out.print(i+" ");
        }
        for (Integer i : greater) {
            System.out.print(i+" ");
        }
    }   
 
 static void printArray(int[] ar) {
         for(int n: ar){
            System.out.print(n+" ");
         }
           System.out.println("");
      }
       
      public static void main(String[] args) {
           Scanner in = new Scanner(System.in);
           int n = in.nextInt();
           int[] ar = new int[n];
           for(int i=0;i<n;i++){
              ar[i]=in.nextInt(); 
           }
           partition(ar);
       }    
   }
