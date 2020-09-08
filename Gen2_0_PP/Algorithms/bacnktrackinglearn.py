def something(a):
    if a > 200:
        return
    print(a)
    a += 1
    if a / 2 == 0:
        a -= 1
        something(a)

something(10)