class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1): return self.intersect(nums2, nums1)
        
        counter = collections.Counter(nums1)
        res = []
        
        for x in nums2:
            if counter[x] > 0:
                res.append(x)
                counter[x] -= 1
        
        return res
        