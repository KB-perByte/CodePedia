'''https://www.facebook.com/hackercup/problem/175329729852444/'''


def main():
    from sys import stdin, stdout
    rl = stdin.readline

    def polyCal():
        N = input()
        for i in xrange(N+1):
            x = int(rl())
        pSize = N % 2
        return "1\n0.0" if pSize == 1 else "0"

    for m in xrange(int(rl())):
        print 'Case #%d: %s' % (m+1, polyCal())
    
main()