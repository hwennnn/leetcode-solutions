class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, n-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < target:
                    l += 1
                
                elif s > target:
                    r -= 1
                
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    
                    l += 1
                    r -= 1
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n-3):
            
            if i > 0 and nums[i] == nums[i-1]: continue
            
            three = self.threeSum(nums[i+1:], target - nums[i])
            for t in three:
                res.append([nums[i]] + t)
            

        return res
                    