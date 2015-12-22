#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

void add(char a[], char b[], char c[], int n) {
    char tmp;
    int i, carry = 0;
    for (i=n; i>=0; i--) {
        tmp = (a[i] - '0') + (b[i] - '0') + carry;
        if (tmp > 1) {
            carry = 1;
            tmp = '0';
        } else {
            tmp = '1';
        }
        c[i+1] = tmp;
    }

    if (carry)
        c[0] = '1';
    else
        c[0] = '0';
}

void print_char(char c[], int index, int n) {
    if (c[0] == '1') {
        printf("%c", c[n+1-index]);
    } else {
        printf("%c", c[n-index]);
    }
}

int main() {
    int n, q;
    // Read N and Q from stdin
    scanf("%d %d", &n, &q);

    char a[n+1], b[n+1], c[n+2];

    // Read the 2 numbers
    scanf("%s %s", a, b);

    char buf[6], x;
    int idx, update = TRUE;
    while (q--) {
        // Read cmd and idx
        scanf("%s %c", buf, &x);

        if (buf[0] == 's') {
            scanf(" %c", &x);
            update = TRUE;
            if (buf[4] == 'a') {
                a[n-idx] = x;
            } else {
                b[n-idx] = x;
            }
        } else {
            if (update) {
                add(a, b, c, n);
                update = FALSE;
            }
            print_char(c, idx, n);
        }
    }

    return 0;
}
