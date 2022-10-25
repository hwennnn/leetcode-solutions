class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        left, right = min(nums), max(nums)
        
        def good(k):
            res = 0
            
            for x, d in zip(nums, cost):
                res += (abs(k - x)) * d
            
            return res
        
        while left < right:
            mid = (left + right) // 2
            
            if good(mid) <= good(mid + 1):
                right = mid
            else:
                left = mid + 1
        
        return good(left)