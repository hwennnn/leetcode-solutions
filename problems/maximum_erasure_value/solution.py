class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = res = count = 0
        s = set()
        
        while j < n:
            while nums[j] in s:
                count -= nums[i]
                s.remove(nums[i])
                i += 1
            
            count += nums[j]
            s.add(nums[j])
            j += 1
            res = max(res, count)
            
        return res