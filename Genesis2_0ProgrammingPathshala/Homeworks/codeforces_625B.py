print(input().count(input())) #this was unexpected 

print("Inputs of test code 2")
#proper way :P
def countStrInsideAStr(sub, mStr): 
    ls = len(sub) 
    lm = len(mStr) 
    res = 0
    for i in range(lm - ls + 1): 
        j = 0
        for j in range(ls): 
            if (mStr[i + j] != sub[j]): 
                break
        if (j == ls - 1): 
            res += 1
            j = 0
    return res 

mainS = input()
sub = input()
print(countStrInsideAStr(sub, mainS))

print("Inputs of testcase 3")
def my_count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in xrange(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    return count

mainS = input()
sub = input()
print(my_count(mainS, sub))


