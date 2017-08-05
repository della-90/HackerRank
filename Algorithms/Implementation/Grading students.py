#!/bin/python3

import sys, math

def round(grade):
    if grade < 38:
        return grade
    
    next_rounding = 5*math.ceil(grade/5)
    return next_rounding if next_rounding-grade < 3 else grade

def solve(grades):
    return map(round, grades)
    
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
