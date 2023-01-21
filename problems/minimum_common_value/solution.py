class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s2 = set(nums2)
        
        for x in nums1:
            if x in s2:
                return x
        
        return -1