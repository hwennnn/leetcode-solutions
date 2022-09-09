class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        keys = sorted(counter.keys())
        
        for x in keys:
            if x > k: break
                
            target = k - x
            
            d = min(counter[target], counter[x])
            res += d
        
        return res // 2