class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        
        for i, x in enumerate(heights):
            while x < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        
        return res