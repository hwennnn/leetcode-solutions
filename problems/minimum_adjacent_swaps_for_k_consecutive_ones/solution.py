class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i,x in enumerate(nums) if x]
        n = len(ones)
        
        prefix = [0]
        for p in ones:
            prefix.append(prefix[-1] + p)
            
        res = float('inf')

        for i in range(n - k + 1):
            right = prefix[i+k] - prefix[k//2 + i]
            left = prefix[(k+1)//2 + i] - prefix[i]
            res = min(res, right - left)
        
        res -= (k//2)*((k+1)//2)
        
        return res