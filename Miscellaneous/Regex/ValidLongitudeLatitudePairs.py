import re
n = int(input())

pattern = r'''
^                       # beginning
\(                      # opening par
(                       # begin latitude group
[-+]?                   # optional sign
[1-9]\d?(?:\.\d+)?       # integer part + optional decimal part
)                       # end latitude
,\s                     # comma and space
(                       # begin longitude
[-+]?                   # same as before
[1-9]\d{0,2}(?:.\d+)?
)                       # end long
\)                      # closing par
$                       # end of string
'''
regex = re.compile(pattern, re.VERBOSE)
for _ in range(0, n):
    s = input()
    result = regex.match(s)
    if (result):
        lat = float(result.group(1))
        lon = float(result.group(2))
        
        
        if (-90 <= lat <= 90 and -180 <= lon <= 180):
            print('Valid')
        else:
            print('Invalid')
    else:
        print("Invalid")
    
