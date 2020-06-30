class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [((target - p)/s, p) for p, s in zip(position, speed)]
        time.sort(key=lambda x:-x[1])
        ans = prev = 0
        for t, _ in time:
            if t > prev:
                prev = t
                ans += 1
        return ans


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        for pos, vel in sorted(zip(position, speed), key=lambda x: -x[0]):
            dist = target - pos
            time = dist / vel
            if not stack or time >= stack[-1]:
                stack.append(time)
        
        return len(stack)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        _time, count = None, 0
        pos = sorted([[position[i], speed[i]]
                for i in range(len(position))], reverse=True)

        for i in range(len([pos])):
            time = (target - pos[i][0]) // pos[i][1]
            if i == 0:
                count = 1
                _time = time
            elif time > _time:
                count += 1
                _time = time
        
        return count

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        _time, count = None, 0
        frame = sorted([[position[i], speed[i]]
                for i in range(len(position))], reverse=True)
        
        
        for i in range(len(frame)):
            time = (target - frame[i][0]) // frame[i][1]
            if i == 0:
                count = 1
                _time = time
            elif time > _time:
                count += 1
                _time = time
        
        return count

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
ss = Solution()
print(ss.carFleet(target, position, speed))
