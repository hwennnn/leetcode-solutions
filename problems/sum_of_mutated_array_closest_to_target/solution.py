class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def getSum(k):
            s = 0
            
            for x in arr:
                s += min(x, k)
            
            return s
        
        left, right = 0, max(arr)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            total = getSum(mid)
            
            if total == target:
                return mid
            elif total < target:
                left = mid + 1
            else:
                right = mid - 1
        
        l2 = left - 1
        
        if abs(getSum(left) - target) < abs(getSum(l2) - target):
            return left
        
        return l2
        