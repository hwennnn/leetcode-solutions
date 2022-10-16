class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        res = [set() for _ in range(2)]
        
        for x in nums1:
            if x not in s2:
                res[0].add(x)
        
        for x in nums2:
            if x not in s1:
                res[1].add(x)
        
        return [list(x) for x in res]