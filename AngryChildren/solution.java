mport java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// The part of the program involving reading from STDIN and writing to STDOUT has been provided by us.

public class Solution {
   static BufferedReader in = new BufferedReader(new InputStreamReader(
         System.in));
   static StringBuilder out = new StringBuilder();

   public static void main(String[] args) throws NumberFormatException, IOException {
      int numPackets = Integer.parseInt(in.readLine());
      int numKids = Integer.parseInt(in.readLine());
      int[] packets = new int[numPackets];
      
      for(int i = 0; i < numPackets; i ++)
      {
         packets[i] = Integer.parseInt(in.readLine());
      }
      
      int unfairness = Integer.MAX_VALUE;
      
        // Write your code here, to process numPackets N, numKids K, and the packets of candies
      // Compute the ideal value for unfairness over here
      Arrays.sort(packets);
       // start with the k lowest packets
       int max = numKids-1;
       int min = 0;
       
       // try to pick packets with more candies
       while (max < packets.length) {
 
           int unf = packets[max]-packets[min];
           if (unf < unfairness) 
               unfairness = unf;
           
           min++;
           max++;
       }
       
       
      System.out.println(unfairness);
   }
    
}

