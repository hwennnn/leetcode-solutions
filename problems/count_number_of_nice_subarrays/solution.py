class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = i = count = 0
        
        for j,x in enumerate(nums):
            if x & 1:
                k -= 1
                count = 0
            
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            
            res += count

        return res