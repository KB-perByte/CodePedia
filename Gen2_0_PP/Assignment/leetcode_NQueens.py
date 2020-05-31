class Solution:
    def solveNQueens(self, n: int) -> int:
        def funcQ(n, bucket1=set(), bucket2=set(), cols=list(), rows=0):
            if rows == n: 
                yield cols[:]
                return

            for col in range(n):
                if (rows + col in bucket1 or rows - col in bucket2) or col in cols:
                    continue

                bucket1.add(rows + col)
                bucket2.add(rows - col)
                cols.append(col)

                yield from funcQ(n, bucket1, bucket2, cols, rows + 1)

                bucket1.remove(rows + col)
                bucket2.remove(rows - col)
                cols.pop()

        return [["."*c + "Q" + "."*((n-c)-1) for c in cols] for cols in funcQ(n)]