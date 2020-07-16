#code
T = int(input())
for i in range(T):
    n=list(input())
    value=0
    for i in range(len(n)):
        d=n.pop()
        if d=='1':
            value=value+pow(2,i)
    if(value%3==0):
        print("1")
    else:
        print("0")

''' #TODO
diff btn the cnt of set bits at odd pos and the cnt of 
set bits at even pos is a mltipl of 3 then the number is a niltpl of 3
'''