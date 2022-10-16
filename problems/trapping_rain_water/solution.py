class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: return 0
        
        i, j = 0, n - 1
        leftMost, rightMost = height[i], height[j]
        res = 0
        
        while i <= j:
            leftMost = max(leftMost, height[i])
            rightMost = max(rightMost, height[j])
            
            if leftMost < rightMost:
                res += leftMost - height[i]
                i += 1
            else:
                res += rightMost - height[j]
                j -= 1
        
        return res