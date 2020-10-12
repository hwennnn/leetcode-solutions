class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        stack = []
        
        for x in nums2:
            
            while stack and stack[-1] < x:
                d[stack.pop()] = x
            
            stack.append(x)
        
        res = []
        for x in nums1:
            res.append(d.get(x, -1))
            
        return res