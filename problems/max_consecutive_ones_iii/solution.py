class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        
        for j in range(n):
            if nums[j] == 0:
                k -= 1
            
            if k < 0:
                if nums[i] == 0:
                    k += 1
                
                i += 1
        
        return j - i + 1