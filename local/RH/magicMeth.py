class Area:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __eq__(self, other):
        if isinstance(other, Area):
            return self.height * self.width == other.height *     other.width
        else:
            return False
        
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width < other.height * other.width
        else:
            return False
        
    def __gt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width > other.height * other.width
        else:
            return False
     
    def __le__(self, other):
        return self == other or self < other
    
    def __ge__(self, other):
        return self == other or self > other
    
a1 = Area(7, 10)
a2 = Area(35, 2)
a3 = Area(8, 9)
print('Testing ==')
print(a1 == 'hello')
print(a1 == a2)
print(a1 == a3)
print('Testing !=')
print(a1 != 'hello')
print(a1 != a2)
print(a1 != a3)
print('Testing <')
print(a1 < 'hello')
print(a1 < a2)
print(a1 < a3)
print('Testing >')
print(a1 > 'hello')
print(a1 > a2)
print(a1 > a3)
print('Testing <=')
print(a1 <= 'hello')
print(a1 <= a2)
print(a1 <= a3)
print('Testing >=')
print(a1 >= 'hello')
print(a1 >= a2)
print(a1 >= a3)