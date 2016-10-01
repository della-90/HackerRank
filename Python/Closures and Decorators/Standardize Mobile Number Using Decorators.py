n = int(raw_input().strip())
numbers = []
for _ in xrange(n):
    numbers.append(raw_input().strip())
    
def wrapper(func):
    def inner(numbers):
        return func(["+91 %s %s" % (number[-10: -5], number[-5:]) for number in numbers])
    return inner

@wrapper
def sort(numbers):
    return sorted(numbers)
    
print "\n".join(sort(numbers))
