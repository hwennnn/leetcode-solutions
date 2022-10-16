class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        A = [0] * (n + 1)
        
        for i, x in enumerate(ranges):
            if x == 0: continue
            
            left = max(i - x, 0)
            A[left] = max(A[left], i + x)
        
        jumps = currStep = currFarthest = i = 0
        
        while i < len(A) and currStep < n:
            jumps += 1
            
            while i < len(A) and i <= currStep:
                currFarthest = max(currFarthest, A[i])
                i += 1
            
            if currStep == currFarthest: return -1
            
            currStep = currFarthest
        
        return jumps