# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
row = raw_input()
print time.strftime('%H:%M:%S', time.strptime(row, '%I:%M:%S%p'))

