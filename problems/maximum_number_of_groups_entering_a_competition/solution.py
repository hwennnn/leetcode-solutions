class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        def good(k):
            return (k * (k + 1)) // 2 <= n
        
        left, right = 0, n
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if good(mid):
                left = mid
            else:
                right = mid - 1

        return left