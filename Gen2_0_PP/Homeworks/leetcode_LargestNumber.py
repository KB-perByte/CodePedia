import functools
        def comparator(s1, s2):
            if int(s1+s2) < int(s2+s1):
                return -1
            if int(s1+s2) > int(s2+s1):
                return 1
            return 0
        
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = functools.cmp_to_key(comparator),  reverse = True)
        ans = '0' if nums[0] == '0' else ''.join(nums)      # if the biggest number after sorting is 0 in first position, then rest all will also be 0's so return 0
        return ans