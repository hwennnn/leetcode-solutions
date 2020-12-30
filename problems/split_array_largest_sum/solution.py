class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def good(x):
            total = 0
            a = 1
            
            for num in nums:
                total += num
                if total > x:
                    total = num
                    a += 1
                
                if a > m: return False
            
            return True
        
        left, right = max(nums), 10**8
        
        while left < right:
            mid = (left+right) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left