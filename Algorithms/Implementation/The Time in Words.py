#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

if h > 12:
    h -= 12

result = ""
if m == 0:
    result += numbers[h-1] + " o' clock"
elif m <= 30:
    result += numbers[m-1]
    if (m != 15 and m != 30):
        result += " minute"
        if m > 1:
            result += "s"
    result += " past "
    result += numbers[h-1]
else:
    result += numbers[59-m]
    if m != 45:
        result += " minute"
        if m < 59:
            result += "s"
    result += " to "
    result += numbers[h]
print result
