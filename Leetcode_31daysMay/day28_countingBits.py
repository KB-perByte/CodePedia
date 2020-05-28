class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        
def countBits(self, num: int) -> List[int]:
    return list(map(lambda x:bin(x).count('1'), range(num+1)))

def countBits(self, num: int) -> List[int]:
    counter = [0]
    while len(counter) < num+1:
        counter.extend([i+1 for i in counter])
    return counter[:num+1]

def countBits(self, num: int) -> List[int]:
    nextOrder = 2
    tracker = 0
    counter = [0]*(num+1)

    for i in range(1, num+1):
        if i == nextOrder:
            nextOrder *= 2
            tracker = 0
        counter[i] = counter[tracker] + 1
        tracker += 1
    return counter
