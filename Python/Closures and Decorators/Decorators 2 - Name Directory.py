# Enter your code here. Read input from STDIN. Print output to STDOUT

people = [tuple(raw_input().split()) for _ in xrange(int(raw_input().strip()))]

def wrapper(func):
    def inner(people):
        return func(sorted(people, key=lambda x: x[2]))
    return inner
    
@wrapper
def sort(people):
    return ["%s %s %s" % ("Mr." if p[3] == 'M' else 'Ms.', p[0], p[1]) for p in people]
    
print "\n".join(sort(people))
