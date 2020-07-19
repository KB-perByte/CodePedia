class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best: int = 0
        x: Dict[int, int] = {i: 1 for i in nums}
        print(x)
        for i in list(x.keys()):
            if i not in x:
                continue
            counter: int = 1
            j: int = 1
            while i + j in x:
                counter += 1
                del x[i + j]
                j += 1
            j = 1
            while i - j in x:
                counter += 1
                del x[i - j]
                j += 1
            del x[i]

            best = max(best, counter)
            if not x:
                break

        return best