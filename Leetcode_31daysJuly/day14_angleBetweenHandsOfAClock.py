class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min((30*hour-5.5*minutes)%360, (5.5*minutes-30*hour)%360)