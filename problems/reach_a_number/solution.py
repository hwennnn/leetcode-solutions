class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = c = 0
        
        while c < target:
            step += 1
            c += step
        
        while (c - target) % 2 != 0:
            step += 1
            c += step
        
        return step