s = []
for t in raw_input():
    if len(s) < 1:
        s.append(t)
    elif t == s[-1]:
        s.pop()
    else:
        s.append(t)
print ''.join(s)