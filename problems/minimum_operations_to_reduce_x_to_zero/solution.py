class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x: return n
        
        target = total - x
        mp = collections.defaultdict(int)
        mp[0] = -1
        c = 0
        res = float('-inf')
        
        for i,num in enumerate(nums):
            c += num
            if c - target in mp:
                res = max(res, i - mp[c-target])
            
            if c not in mp:
                mp[c] = i
        
        return n - res if res != float('-inf') else -1