#!/bin/python

import sys

n = long(raw_input().strip())

# Let's consider two bits, namely "a" and "b"
# The XOR operation equals the SUM operation only when "a" is 0 and "b" is either 0 or 1.
# Hence, for each zero bit in "n" we have 2 possible values for the corresponding bit in "x".
#
# The total result, hence, is 2^(number of zero bits in "n")
#
# The only edge case is when "n" is 0, because we need "x" to be smaller or equal to "n".
# In this case the answer is 1.

if n == 0:
    print 1
else:
    # get the binary representation of the number, excluding the prefix "0b
    binary = bin(n)[2:]

    # count number of zero bits
    zeros = sum(1 for c in binary if c == '0')

    print 2**zeros
