class Solution:
    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
                
            j, k = i + 1, n - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == target:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    
                    j += 1
                    k -= 1
                elif s > target:
                    k -= 1
                else:
                    j += 1
        
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
                
            for arr in self.threeSum(nums[i + 1:], target - nums[i]):
                res.append([nums[i]] + arr)
        
        return res
            