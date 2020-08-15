#pure multiple inheritance DLR Algorithm

class A:
    pass

class B:
    pass

class C(A,B):
    pass

class D(C,A,B):
    pass

abcd = D()
print(D.__mro__)

#pure multilevel Interitance

class X:
    pass

class Y(X):
    pass

class Z(Y):
    pass

xyz = Z()

print(Z.__mro__)































































































































































