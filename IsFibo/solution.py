import math
for line in range(int(raw_input())):
    x = int(raw_input())
    plus = math.sqrt(5* x**2 +4)
    minus = math.sqrt(5* x**2 -4)
    result = plus.is_integer() or minus.is_integer()
    if result:
        print("IsFibo")
    else:
        print("IsNotFibo")
    
