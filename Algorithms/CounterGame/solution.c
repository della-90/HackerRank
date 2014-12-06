#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define RICHARD 1
#define LOUISE 0

int main() {
    int lines;
    scanf("%d", &lines);
    while (lines--) {
        // Scan the number
        unsigned long long n;
        scanf("%llu", &n);
        
        int turn = LOUISE;
        // Main loop
        while (n != 1) {
            
            // Chech if n is power of 2
            int bits = -1;
            unsigned long long tmp = n;
            while (tmp) {
                // half tmp
                tmp = tmp >> 1;
                bits++;
            }
            
            unsigned long long greatest = (unsigned long long) 1 << bits;
            
            if (n == greatest) {
                n = n>>1;
            } else {
                n -= greatest;
            }
            
            // update turn
            turn = (turn+1)%2;
        }
        
        /*
         * Now n is 1. The player which should play now loses.
         */
        if (turn == LOUISE) {
            printf("%s\n", "Richard");
        } else {
            printf("%s\n", "Louise");
        }
    }
    return 0;
}

