noOfInput = int(input())

while noOfInput:
    noOfInput-=1
    k, d0, d1 = map(int, input().split())
    s, a = 0, 0
    rem = [0, 2, 0, 2]
    s = (d0+d1)%10
    if k > 2:
        if s == 0:
            a = (d0+d1)%3
        elif s == 1:
            a = ((2*((k-3)//4))%3 + (d0+d1+1)%3 + rem[((k-3)%4)])%3
        elif s == 2:
            a = ((2*((k-2)//4))%3 + (d0+d1)%3 + rem[((k-2)%4)])%3
        elif s == 3:
            a = ((2*((k-4)//4))%3 + (d0+d1+3+6)%3 + rem[((k-4)%4)])%3
        elif s == 4:
            a = ((2*((k-5)//4))%3 + (d0+d1+4+8+6)%3 + rem[((k-5)%4)])%3
        elif s == 5:
            a = (d0+d1+5)%3
        elif s == 6:
            a = ((2*((k-3)//4))%3 + (d0+d1+6)%3 + rem[((k-3)%4)])%3
        elif s == 7:
            a = ((2*((k-6)//4))%3 + (d0+d1+7+4+8+6)%3 + rem[((k-6)%4)])%3
        elif s == 8:
            a = ((2*((k-4)//4))%3 + (d0+d1+8+6)%3 + rem[((k-4)%4)])%3
        elif s == 9:
            a = ((2*((k-5)//4))%3 + (d0+d1+9+8+6)%3 + rem[((k-5)%4)])%3
    else:
        a = (d0+d1)%3
    if a:
        print("NO")
    else:
        print("YES")