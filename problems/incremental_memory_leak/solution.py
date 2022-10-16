class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        t = 1
        sticks = [m1, m2]
        
        while True:
            if t > max(sticks):
                return [t, *sticks]
            
            if sticks[0] >= sticks[1]:
                sticks[0] -= t
            else:
                sticks[1] -= t
            
            t += 1
            