class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x: return n
        target = total - x
        
        res = float('-inf')
        s = 0
        mp = collections.defaultdict(int)
        mp[0] = -1
        
        for i,num in enumerate(nums):
            s += num
            
            if s - target in mp:
                res = max(res, i - mp[s-target])
            
            if s not in mp: mp[s] = i
        
        return n - res if res != float('-inf') else -1