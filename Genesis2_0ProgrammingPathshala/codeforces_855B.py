'''
https://codeforces.com/problemset/problem/855/B
'''

def main():
    a , b, c, x = [], [], [], []
    n, p, q, r = map(int,input().split())
    x = map(int,input().split())

    N = len(x)//2

    for i in x:
        a.append(p * i)
        b.append(q * i)
        c.append(r * i)

    print(max(a) + max(b) + max(c))


main()
