#Homework Array-1

def checkInclusion(s1, s2):    
    subStr = [ord(x) - ord('a') for x in s1]
    mainStr = [ord(x) - ord('a') for x in s2]
    
    target = [0] * 26
    for x in subStr:
        target[x] += 1
    
    window = [0] * 26
    for i, x in enumerate(mainStr):
        window[x] += 1
        if i >= len(subStr):
            window[mainStr[i - len(subStr)]] -= 1
        if window == target:
            return True
    return False

checkInclusion('ab', 'aababaffjdfkjsn')