from math import sqrt

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
        
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary * other.real)
    
    def __str__(self):
        return "%.2f%s%.2fi" % (self.real, "+" if self.imaginary >= 0 else '', self.imaginary)
    
    def __div__(self, other):
        return self * other.reciprocal()
        
    def reciprocal(self):
        return Complex(self.real / (self.real**2 + self.imaginary**2), -self.imaginary / (self.real**2 + self.imaginary**2))
    
    def modulus(self):
        return Complex(sqrt(self.real**2 + self.imaginary**2), 0)
        
real, imaginary = map(float, raw_input().split())
c = Complex(real, imaginary)
real, imaginary = map(float, raw_input().split())
d = Complex(real, imaginary)

print c + d
print c - d
print c * d
print c / d
print c.modulus()
print d.modulus()
        
