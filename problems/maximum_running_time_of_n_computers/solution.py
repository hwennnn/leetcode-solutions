class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def good(k):
            target = n * k
            have = 0
            
            for x in batteries:
                have += min(x, k)

            return have >= target
        
        total = sum(batteries)
        
        left, right = 0, total // n
        res = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res