class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour%12) * 30 + (minutes/60 * 30)
        
        m = minutes/60 * 360
        
        angle = abs(h-m)
        
        if angle > 180:
            angle = 360 - angle
        
        return angle