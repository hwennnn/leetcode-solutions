class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def good(x):
            s = 0
            curr = 1
            
            for num in nums:
                s += num
                
                if s > x:
                    s = num
                    curr += 1
                
                if curr > m: return False
            
            return True
        
        left, right = max(nums), (10 ** 6) * 50
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left