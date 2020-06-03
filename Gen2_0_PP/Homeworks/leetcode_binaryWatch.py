class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        m = [0 for i in range(10)]
        h = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        res = []
        
        def time(x, m, lit, n):
            if lit == n:
                hour = 0
                minute = 0
                for i in range(4):
                    if m[i] == 1:
                        hour += h[i]
                for j in range(4, 10):
                    if m[j] == 1:
                        minute += h[j]
                if hour < 12 and minute < 60:
                    if minute < 10:
                        res.append(str(hour % 12) + ':0' + str(minute))
                    else:
                        res.append(str(hour % 12) + ':' + str(minute))
                return

            for i in range(x, 10):
                    m[i] = 1
                    time(i+1, m, lit+1, n)
                    m[i] = 0
        time(0, m, 0, n)
        return res