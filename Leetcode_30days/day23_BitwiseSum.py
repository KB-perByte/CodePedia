def rangeBitwiseAnd1(self, m, n):
    d = n-m
    p = 0
    while d:
        p += 1
        d /= 2
    return ((m&n)>>p)<<p
    
def rangeBitwiseAnd2(self, m, n):
    if m == n:
        return m
    return self.rangeBitwiseAnd(m>>1, n>>1) << 1
    
def rangeBitwiseAnd3(self, m, n):
    p = 0
    while m != n:
        m >>= 1
        n >>= 1
        p += 1
    return m << p
    
def rangeBitwiseAnd(self, m, n):
    p = 0
    q = m^n
    while q:
        p += 1
        q >>= 1
    return ((m&n)>>p)<<p