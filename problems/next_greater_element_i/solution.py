class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        
        for x in nums2:
            while stack and x > stack[-1]:
                greater[stack.pop()] = x
            
            stack.append(x)
        
        for i, x in enumerate(nums1):
            nums1[i] = greater.get(x, -1)
        
        return nums1