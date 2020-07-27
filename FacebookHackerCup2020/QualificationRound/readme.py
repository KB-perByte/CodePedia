import sys
# For getting input
sys.stdin = open('FacebookHackerCup2020/QualificationRound/alchemy_validation_input.txt', 'r')
for line in sys.stdin:
    print(line)
# Printing the Output
sys.stdout = open('sample.txt', 'w')



'''
You just write simple program and then run it from command line in any platform like Windows/ Linux.

python program.py < input.txt > output.txt

<,> are redirection operators which simply redirects the stdin and stdout to input.txt and output.txt. This is the easiest way.

Alternatively, you can do the following

import sys
sys.stdin=open(‘input.txt’,‘r’)
sys.stdout=open(‘output.txt’,‘w’)

Alternatively you can do the following
input=open(‘input.txt’,‘r’)
ouput=open(‘ouput.txt’,‘w’)
n=input.read()
output.write(n)

I prefer method 1 as it is simple and no need of file handling and this helps a lot in Codejam, FaceBook HackerCup. Hope it helps
'''