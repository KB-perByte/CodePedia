#Better say python data models than dunder methords

class Polynomail:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomail(*(x + y for x, y in zip (self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

p1 =Polynomail(1,2,3)
p2 =Polynomail(2,3,4)

print(p1)

k = p1 + p2
print(k)
