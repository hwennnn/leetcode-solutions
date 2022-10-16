from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        
        left = SortedList(nums[:n])
        right = SortedList(nums[n:])
        sumLeft = sum(left)
        sumRight = sum(right[-n:])
        res = sumLeft - sumRight
        
        for i in range(n, 2 * n):
            index = right.bisect_left(nums[i])
            
            if index >= len(right) - n:
                sumRight -= nums[i]
                sumRight += right[-n-1]
            
            index = left.bisect_left(nums[i])
            
            if index < n:
                sumLeft += nums[i]
                sumLeft -= left[n - 1]
            
            right.discard(nums[i])
            left.add(nums[i])
            
            res = min(res, sumLeft - sumRight)
        
        return res
        