def fibonacci():
    a=0
    b=1 
    while True:
        #print(a)
        yield a
        future = a + b 
        a = b
        b = future


# for values in fibonacci():
#     print(values)

def squareIt(n):
    i = 0
    flag = True
    while flag:
        yield i*i
        i=i+1
        if i > n:
            flag = False

for sq in squareIt(100):
    print(sq)


