class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[n-1]
        
        for i in range(n-2):
            
            l, r = i+1, n-1
            
            while l < r:
                c = nums[i] + nums[l] + nums[r]
                if abs(target-c) < abs(target-res):
                    res = c
                
                if c > target: r -= 1
                elif c < target: l += 1
                else: return res
                    
                
                    
        return res
                    