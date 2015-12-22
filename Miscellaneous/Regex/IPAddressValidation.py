import re

patternIPv4 = r'''
^
(
    (\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])   # 1 byte
    \.
){3}
(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])
$
'''
    
patternIPv6 = r'''
^
(?:[0-9a-f]{1,4}:){7}
[a-f0-9]{1,4}
$
'''
ipv4 = re.compile(patternIPv4, re.X)
ipv6 = re.compile(patternIPv6, re.X)
for _ in range(int(input())):
    s = input()
    if (ipv4.match(s)):
        print('IPv4')
    elif (ipv6.match(s)):
        print('IPv6')
    else:
        print('Neither')
 
    
