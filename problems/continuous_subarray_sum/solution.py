class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = {0: -1}
        c = 0
        
        for i, x in enumerate(nums):
            c += x
            if k != 0:
                c %= k
            
            if c in prefix:
                if i - prefix[c] > 1:
                    return True
            else:
                prefix[c] = i
    
        return False
        