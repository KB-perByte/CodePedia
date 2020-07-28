class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(collections.Counter(tasks).values())
        print(count)
        max_num = max(count)
        print(max_num)
        max_num_count = count.count(max_num)
        print(max_num_count)
        return max(len(tasks), (n+1)*(max_num-1)+ max_num_count)