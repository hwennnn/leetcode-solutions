class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            j, k = i + 1, n - 1
            
            while j < k:
                ssum = nums[i] + nums[j] + nums[k]
                
                if ssum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    
                    k -= 1
                    j += 1
                elif ssum > 0:
                    k -= 1
                else:
                    j += 1
        
        return res
        