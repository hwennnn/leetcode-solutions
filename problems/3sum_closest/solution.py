class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            
            while j < k:
                ss = nums[i] + nums[j] + nums[k]
                if abs(ss - target) < abs(res - target):
                    res = ss
                
                if ss == target: 
                    return ss
                elif ss > target:
                    k -= 1
                else:
                    j += 1
        
        return res