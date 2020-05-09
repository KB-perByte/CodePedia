class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countEle(matrix, md):
            cnt = 0
            for k in matrix:
                for col in k:
                    if col <= md:
                        cnt += 1
            print(cnt)
            return cnt

        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            cnt = countEle(matrix, mid)
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        return l


class Solution2(object):
    def kthSmallest(self, matrix, k):
        import heapq
        val = [k for row in matrix for k in row]
        heapq.heapify(val)
        for _ in range(k):
            ans = heapq.heappop(val)
        return ans