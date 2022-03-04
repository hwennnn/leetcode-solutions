class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        index = {x: i for i, x in enumerate(nums1)}
        res = [-1] * n1
        
        stack = []
        
        for i, x in enumerate(nums2):
            while stack and x > nums2[stack[-1]]:
                num = nums2[stack.pop()]
                if num in index:
                    res[index[num]] = x
            stack.append(i)
            
        return res