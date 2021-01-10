def printPatternStair(ln):
    for i in range(1, ln+1):
        print('*'*i)

printPatternStair(6)

def printPatternDiamond(ln): # LOL 
    for i in range(1, (ln+1)*2):
        print( ' ' * (ln-i) + "* " * i)

printPatternDiamond(6)

