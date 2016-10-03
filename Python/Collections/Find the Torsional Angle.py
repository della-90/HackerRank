from math import sqrt, acos, degrees

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y-other.y, self.z - other.z)
        
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        return Point(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
        
    def modulus(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    
A = Point(*map(float, raw_input().split()))
B = Point(*map(float, raw_input().split()))
C = Point(*map(float, raw_input().split()))
D = Point(*map(float, raw_input().split()))
    
    
AB = A - B
BC = B - C
CD = C - D
X = AB.cross(BC)
Y = BC.cross(CD)
print "%.2f" % degrees(acos(X.dot(Y) / (X.modulus() * Y.modulus())))
