class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total == x: return n
        
        res = float('-inf')
        target = total - x
        mp = {0:-1}
        curr = 0
        
        for i, x in enumerate(nums):
            curr += x
            
            if curr - target in mp:
                res = max(res, i - mp[curr - target])
            
            if curr not in mp:
                mp[curr] = i
        
        return -1 if res == float('-inf') else n - res