# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

lan = 'Python'
for line in sys.stdin:
    if '#include' in line:
        lan = 'C'
        break
    if 'import java' in line:
        lan = 'Java'
        break
print lan
