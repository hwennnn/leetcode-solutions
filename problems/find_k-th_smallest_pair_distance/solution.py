class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def enough(x):
            count = i = j = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= x:
                    j += 1
                
                count += j - i - 1
                i += 1
            
            return count >= k
        
        n = len(nums)
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            