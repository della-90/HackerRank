# Let's consider the following matrix
#
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
#
# Let's consider element 1: you can swap it with 4, 13, 16.
# Let's consider element 2: you can swap it with 3, 6, 7.
#
# In general if you have a 2n x 2n matrix, you can swap element in position (i; j) with:
# element in position (i; 2n-j)
# element in position (2n-i; j)
# element in position (2n-i; 2n-j)
#
# To find the solution, you need to find for each element in the n x n submatrix the highest replacement possible.

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    matrix = [map(int, raw_input().split()) for _ in xrange(2*n)]
    
    total = 0
    for i in xrange(n):
        for j in xrange(n):
            total += max(matrix[i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])
    print total
