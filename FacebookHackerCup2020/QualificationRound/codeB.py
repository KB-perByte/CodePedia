from collections import Counter

testCase = int(input())
tt = 0
while(tt<testCase):
    N = int(input())
    _shards = input()
    
    #print(len(_shards))
    dicShrads = Counter(_shards)
    #print(abs(dicShrads.get('A',0) - dicShrads.get('B',0)))

    if abs(dicShrads.get('A',0) - dicShrads.get('B',0)) == 1 :
       print('Case #'+ str(tt+1)+ ':')
       print('Y')
    else:
       print('Case #'+ str(tt+1)+ ':')
       print('N')
    tt+=1