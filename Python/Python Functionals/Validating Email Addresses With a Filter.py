import re

regex = re.compile(r'^[-\w]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$')

email_filter = lambda x: regex.match(x)

emails = []
for _ in xrange(int(raw_input())):
    emails.append(raw_input())
    
print sorted(filter(email_filter, emails))
    
