class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        c = collections.Counter(nums)
        res = 0
        
        for x in nums:
            if c[x] > 0 and c[k-x] > 0:
                c[x] -= 1
                c[k-x] -= 1
                res += 1
                
                if c[x] < 0:
                    res -= 1
        
        return res
        
        