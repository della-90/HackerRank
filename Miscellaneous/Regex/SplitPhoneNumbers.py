import re
n = int(input())
pattern = r'(?P<cc>\d{1,3}).(?P<lac>\d{1,3}).(?P<n>\d{4,10})'
regex = re.compile(pattern)
for i in range(0, n):
    s = input()
    result = regex.match(s)
    if (result):
        print('CountryCode={},LocalAreaCode={},Number={}'.format(result.group('cc'), result.group('lac'), result.group('n')))
